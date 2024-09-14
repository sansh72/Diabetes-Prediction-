from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import pandas as pd
import os
import numpy as np  # Import numpy to handle conversion

app = Flask(__name__)
CORS(app)

# Load your trained model
model = joblib.load('model_filename.pkl')

@app.route('/predict', methods=['POST'])
@app.route('/')
def home():
    return render_template('index.html')
    
def predict():
    data = request.json

    # Create DataFrame from input data
    columns = ["crim", "zn", "indus", "chas", "nox", "rm", "age", "dis", "rad", "tax", "ptratio", "b", "lstat"]
    input_data = [[
        data['crim'], data['zn'], data['indus'], data['chas'], data['nox'],
        data['rm'], data['age'], data['dis'], data['rad'], data['tax'],
        data['ptratio'], data['b'], data['lstat']
    ]]

    df_data = pd.DataFrame(input_data, columns=columns)
    df_data["chas"] = pd.to_numeric(df_data["chas"], errors='coerce')

    # Predict using the model
    result = model.predict(df_data)

    # Convert numpy.float32 to Python float
    prediction = float(result[0])*1000

    # Return the prediction as a JSON response
    return jsonify({'price': prediction})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Use the port set by the environment, default to 5000
    app.run(host='0.0.0.0', port=port, debug=True)
