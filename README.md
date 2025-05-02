# 🌾 Crop Recommendation System

A Machine Learning-based web application that recommends the most suitable crop to grow based on environmental conditions such as soil type, temperature, humidity, and rainfall.

## 🚀 Features

- Predicts the best crop to cultivate using ML models
- Takes input parameters like nitrogen, phosphorus, potassium, temperature, humidity, pH, and rainfall
- Simple and interactive web interface
- Built with Python, scikit-learn, and Flask

## 🛠️ Tech Stack

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Python, Flask
- **Machine Learning**: scikit-learn, pandas, NumPy
- **Deployment**: GitHub / local server

## 📦 Installation

1. Clone the repository:
```
git clone https://github.com/Garv-Sehgal/Crop-Recommendation-System.git
cd Crop-Recommendation-System
```
2. Create a virtual environment and activate it:
```
python -m venv venv
venv\Scripts\activate   # For Windows
```
3. Install dependencies:
```
pip install -r requirements.txt
```
4. Run the application:
```
python manage.py runserver
```
Then, open your browser and go to http://127.0.0.1:8000/

## 🧪 Example Input
| Feature        | Example Value |
| -------------- | ------------- |
| Nitrogen (N)   | 90            |
| Phosphorus (P) | 42            |
| Potassium (K)  | 43            |
| Temperature    | 22            |
| Humidity       | 80%           |
| pH             | 6.5           |
| Rainfall       | 200           |

**Output: Rice**

# 📊 Model Training

- Dataset: Kaggle Crop Recommendation Dataset
- Algorithm used: Random Forest Classifier
- Accuracy: ~98%
- The model is trained using standard ML practices: data preprocessing, model training, evaluation, and saving via pickle.

# 💡 Future Improvements

- Add region-based or season-specific recommendations
- Use a live weather API for real-time input
- Deploy the app using cloud platforms like Heroku or AWS
- Add fertilizer and pesticide suggestions
