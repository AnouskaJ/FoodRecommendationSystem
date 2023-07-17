from flask import Flask, render_template, request, jsonify
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import string

app = Flask(__name__)

df = pd.read_csv('dataset/1662574418893344.csv')

# Cleaning of description
def cleaning(text):
    text = "".join([char for char in text if char not in string.punctuation])
    return text

df['Describe'] = df['Describe'].apply(cleaning)

food_features = ['C_Type','Veg_Non', 'Describe']

def features_column(x):
    return x['C_Type'] + " " + x['Veg_Non'] + " " + x['Describe']

# Column with all the features to dataframe df
df['features'] = df.apply(features_column, axis=1)

# Content-based filtering using advanced features
vect2 = TfidfVectorizer(stop_words='english')
vect_X = vect2.fit_transform(df['features'])
cosine_similarity2 = cosine_similarity(vect_X, vect_X)

food_items = pd.Series(df.index, index=df['Name']).drop_duplicates()

# Content-based recommendation function based on advanced features
def food_recommendations_advanced(title):
    food_index = food_items[title]
    similarity_scores = list(enumerate(cosine_similarity2[food_index]))
    similarity_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)
    most_recommended_scores = similarity_scores[1:6]
    most_recommended_dishes = [df['Name'].iloc[i[0]] for i in most_recommended_scores]
    return most_recommended_dishes

# Route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# Route for handling the form submission and returning recommended dishes
@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.json
    dish_name = data['name'].lower()
    recommended_dishes = food_recommendations_advanced(dish_name)
    return jsonify({'recommended_dishes': recommended_dishes})

if __name__ == '__main__':
    app.run(debug=True)
