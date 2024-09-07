# Diabetes Prediction Web Application

This project is a **Diabetes Prediction Web Application** using a machine learning model built with Python. The web interface allows users to input relevant medical data, and the backend will predict if the person is diabetic or not. The model was built using several libraries, and the web application is powered by **Flask** for the backend and basic HTML/CSS/JavaScript for the frontend.

## Features

- **Machine Learning Model**: A Support Vector Machine (SVM) model was trained to predict diabetes.
- **Simple Web Form**: Users can input their medical data into a web form (Pregnancies, Glucose, Blood Pressure, etc.), and the model will predict whether they are likely to have diabetes.
- **Free to Use**: This web application is free and accessible to anyone.
- **Libraries Used**: Several popular Python libraries were used to build and train the machine learning model.

## Libraries and Tools Used

- **NumPy**: For numerical computations.
- **Pandas**: To handle data manipulation.
- **scikit-learn**: Used for model building, including preprocessing, model training, and evaluation.
  - `StandardScaler`: For data normalization.
  - `SVM`: For building the prediction model.
  - `train_test_split`: For splitting the dataset into training and testing sets.
  - `accuracy_score`: To evaluate the model's performance.
- **Flask**: A micro web framework used to create a RESTful API that serves the model's predictions.
- **HTML/CSS/JavaScript**: Used to build a simple and interactive user interface to collect data and display results.

## How It Works

1. **Data Input**: Users enter the following data via the web form:
   - Pregnancies
   - Glucose Level
   - Blood Pressure
   - Skin Thickness
   - Insulin Level
   - BMI (Body Mass Index)
   - Diabetes Pedigree Function
   - Age
   
2. **Model Prediction**: The user’s input is sent to the Flask API, which processes the data and uses the trained SVM model to predict whether the person is diabetic.

3. **Result Display**: The result (either "The person is diabetic" or "The person isn't diabetic") is displayed on the webpage.

## How to get started
Here are the required libraries that you would need to install
1. pip install numpy pandas scikit-learn flask
2. python app.py


