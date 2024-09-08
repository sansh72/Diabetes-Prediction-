from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import numpy as np
import pandas as pd
import joblib
import os

app = Flask(__name__)
CORS(app)

# Load the trained model and scaler
classifier = joblib.load('model_filename.pkl')
scaler = joblib.load('scaler_filename.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get JSON data from the request
        data = request.get_json()
        str_data = str(data)
        
        with open('output.txt', 'w') as file:
            file.write(str_data)
        
        # Convert JSON data to DataFrame
        df = pd.DataFrame([data])  # Wrap in a list to create a DataFrame with one row

        # Check if 'Outcome' column exists and drop it
        if 'Outcome' in df.columns:
            df = df.drop(columns='Outcome')

        # Convert to numpy array and reshape
        numpy_array = np.asarray(df)
        numpy_reshaped = numpy_array.reshape(1, -1)

        # Standardize the input data
        std_data = scaler.transform(numpy_reshaped)

        # Make prediction
        prediction = classifier.predict(std_data)

        # Return the result
        if prediction[0] == 1:
            result = "The person is diabetic"
        else:
            result = "The person isn't diabetic"

        return jsonify({'result': result})
    
    except Exception as e:
        app.logger.error(f'Error in predict function: {e}')
        return jsonify({'error': 'An error occurred during prediction'}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Use the port set by the environment, default to 5000
    app.run(host='0.0.0.0', port=port, debug=True)

