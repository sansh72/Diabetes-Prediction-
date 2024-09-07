from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS
import numpy as np
import pandas as pd
import joblib
import time

app = Flask(__name__)
CORS(app)

# Load the trained model and scaler
classifier = joblib.load('model_filename.pkl')
scaler = joblib.load('scaler_filename.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    # Get JSON data from the request
    data = request.get_json()
    str_data = str(data)

    with open('output.txt', 'w') as file:
        file.write(str_data)
    # Convert JSON data to DataFrame

    df = pd.DataFrame([data])  # Wrap in a list to create a DataFrame with one row
    df = df.drop(columns='Outcome',axis = 1)

    # Convert to numpy array and reshape
    numpy_array = np.asarray(df)
    numpy_reshaped = numpy_array.reshape(1, -1)

    # Standardize the input data
    scaler.fit(numpy_reshaped)
    std_data = scaler.transform(numpy_reshaped)

    # Make prediction
    prediction = classifier.predict(std_data)

    # Return the result
    if prediction[0] == 1:
        result = "The person is diabetic"
    else:
        result = "The person isn't diabetic"

    return jsonify({'result': result})


if __name__ == '__main__':
    app.run(debug=True)
