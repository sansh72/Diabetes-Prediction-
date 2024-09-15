from flask import Flask, request, jsonify, render_template
from flask_cors import CORS  # Import CORS
import numpy as np
import pandas as pd
import joblib
import os

app = Flask(__name__)
CORS(app)

# Load the trained model and scaler
classifier = joblib.load('model_filename.pkl')
scaler = joblib.load('scaler_filename.pkl')

@app.route('/predict', methods=['POST'])
@app.route('/')
def home():
    return render_template('index.html')
def predict():
    # Get JSON data from the request
    data = request.get_json()
    str_data = str(data)

    with open('output.txt', 'w') as file:
        file.write(str_data)
    
    # Convert JSON data to DataFrame
    df = pd.DataFrame([data])  # Wrap in a list to create a DataFrame with one row
    df = df.drop(columns='Outcome', axis=1)  # Drop the 'Outcome' column if it exists

    # Convert to numpy array and reshape
    numpy_array = np.asarray(df)
    numpy_reshaped = numpy_array.reshape(1, -1)

    # Standardize the input data
    std_data = scaler.transform(numpy_reshaped)  # Use only transform, not fit

    # Make prediction
    prediction = classifier.predict(std_data)

    # Return the result
    if prediction[0] == 1:
        result = "The person is diabetic"
    else:
        result = "The person isn't diabetic"

    return jsonify({'result': result})


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Use the port set by the environment, default to 5000
    app.run(host='0.0.0.0', port=port, debug=True)
