---

# 🍽️ Food Recommendation System  

Welcome to the **Food Recommendation System**! This system provides personalized dish recommendations based on textual descriptions and categorical features. Using **content-based filtering**, it helps users discover new dishes similar to their preferences.  

---

## 🚀 Features  

### 🔹 **Basic Recommendation**  
✅ Recommends **similar dishes** based on the description of a given dish.  
✅ Uses **text vectorization** and similarity measurements to find matches.  

### 🔹 **Advanced Recommendation**  
✅ Suggests dishes based on:  
- **Category** (e.g., dessert, main course, appetizer) 🍰🍛🥗  
- **Vegetarian or Non-Vegetarian Classification** 🥦🍖  
- **Detailed Description Matching** 📖  

---

## 🛠️ Technologies Used  

| Technology | Purpose |
|------------|---------|
| 🐍 **Python** | Core programming language |
| 🌍 **Flask** | Backend API framework |
| 🔢 **Scikit-learn** | Text vectorization & similarity calculations |
| 📊 **Pandas** | Data manipulation & analysis |

---

## 📽️ Demo Video  

🔗 **Check out the working demo here:**  
[![Video Display](https://github.com/AnouskaJ/FoodRecommendationSystem/assets/82711261/e9397460-9bba-47fa-9b40-79cdcb1c9d43)](https://github.com/AnouskaJ/FoodRecommendationSystem/assets/82711261/e9397460-9bba-47fa-9b40-79cdcb1c9d43)

---

## 📦 Installation & Setup  

### 🔹 Prerequisites  
Ensure you have **Python 3.x** installed on your system.  

### 🔹 Steps to Run the Project  

1️⃣ **Clone the repository**  
```bash
git clone https://github.com/AnouskaJ/FoodRecommendationSystem.git
cd FoodRecommendationSystem
```

2️⃣ **Create a virtual environment (optional but recommended)**  
```bash
python -m venv myenv
source myenv/bin/activate  # On macOS/Linux
myenv\Scripts\activate  # On Windows
```

3️⃣ **Install dependencies**  
```bash
pip install -r requirements.txt
```

4️⃣ **Run the Flask server**  
```bash
python app.py
```

5️⃣ **Access the API**  
By default, the server runs at:  
🌍 `http://127.0.0.1:5000/`

---

## 📡 API Endpoints  

### 🔹 **Basic Recommendation**  
**Endpoint:** `/recommend/basic`  
**Method:** `POST`  
**Request Format (JSON):**  
```json
{
  "dish_name": "Pasta Alfredo"
}
```
**Response Format (JSON):**  
```json
{
  "recommended_dishes": ["Spaghetti Carbonara", "Mac & Cheese", "Penne Arrabbiata"]
}
```

### 🔹 **Advanced Recommendation**  
**Endpoint:** `/recommend/advanced`  
**Method:** `POST`  
**Request Format (JSON):**  
```json
{
  "dish_name": "Paneer Butter Masala",
  "category": "Main Course",
  "vegetarian": true
}
```
**Response Format (JSON):**  
```json
{
  "recommended_dishes": ["Shahi Paneer", "Dal Makhani", "Aloo Gobi"]
}
```

---

## 🎯 Future Enhancements  

🔹 Add **collaborative filtering** for improved recommendations  
🔹 Include **user ratings and feedback system** ⭐  
🔹 Integrate **real-time web scraping** for recipe suggestions  

---

## 🤝 Contributing  

We welcome contributions! 🛠️  
1️⃣ Fork the repository  
2️⃣ Create a feature branch (`git checkout -b feature-name`)  
3️⃣ Commit your changes (`git commit -m "Added feature XYZ"`)  
4️⃣ Push to your branch (`git push origin feature-name`)  
5️⃣ Open a **Pull Request**  

---


💡 **Enjoy using the Food Recommendation System! 🍕🥗🍣 Let us know your thoughts!** 🚀  

---
