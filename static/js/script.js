document.getElementById('diabetesForm').addEventListener('submit', function (event) {
    event.preventDefault();
  
    // Collect input values from the form
    const data = {
        Pregnancies: parseFloat(document.getElementById('pregnancies').value),
        Glucose: parseFloat(document.getElementById('glucose').value),
        BloodPressure: parseFloat(document.getElementById('bloodPressure').value),
        SkinThickness: parseFloat(document.getElementById('skinThickness').value),
        Insulin: parseFloat(document.getElementById('insulin').value),
        BMI: parseFloat(document.getElementById('bmi').value),
        DiabetesPedigreeFunction: parseFloat(document.getElementById('diabetesPedigreeFunction').value),
        Age: parseFloat(document.getElementById('age').value)
    };
  
    // Make a POST request to the Flask API
    fetch('https://diabetes-prediction-58g9.onrender.com/predict', {  // Update this URL to your Render deployment
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)  // Send data as a JSON string
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(result => {
        console.log('Success:', result);
  
        // Display the prediction result on the webpage
        const resultElement = document.getElementById('result');
        resultElement.innerText = result.result;
  
        // Show the result for 3 minutes (180,000 milliseconds), then clear it
        setTimeout(() => {
            resultElement.innerText = '';
        }, 180000);  // 180000 ms = 3 minutes
    })
    .catch((error) => {
        console.error('Error:', error);
  
        // Display the error message to the user
        const resultElement = document.getElementById('result');
        resultElement.innerText = 'An error occurred while predicting. Please try again.';
  
        // Hide the error message after 3 minutes
        setTimeout(() => {
            resultElement.innerText = '';
        }, 180000);  // 180000 ms = 3 minutes
    });
});

  
