const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');
const fs = require('fs');
const { exec } = require('child_process');
const createCsvWriter = require('csv-writer').createObjectCsvWriter;

const app = express();
const port = 5000;

// Middleware
app.use(bodyParser.json());
app.use(cors());

// Set up the CSV writer
const csvWriter = createCsvWriter({
  path: 'diabetes_data.csv',
  header: [
    { id: 'pregnancies', title: 'Pregnancies' },
    { id: 'glucose', title: 'Glucose' },
    { id: 'bloodPressure', title: 'BloodPressure' },
    { id: 'skinThickness', title: 'SkinThickness' },
    { id: 'insulin', title: 'Insulin' },
    { id: 'bmi', title: 'BMI' },
    { id: 'diabetesPedigreeFunction', title: 'DiabetesPedigreeFunction' },
    { id: 'age', title: 'Age' }
  ],
  append: true // If file exists, append to it; otherwise, create a new file
});

// Route to handle form data and predict diabetes
app.post('/api/save-data', (req, res) => {
  const data = req.body;
csv = "jupter.ipynb"
  // Save the data to CSV
  csvWriter.writeRecords([data])
    .then(() => {
      console.log('Data saved to CSV file');

      // Call the Python script to make predictions
      exec('jupter.ipynb', (error, stdout, stderr) => {
        if (error) {
          console.error(`Error executing Python script: ${error.message}`);
          return res.status(500).send('Error executing Python script');
        }

        if (stderr) {
          console.error(`stderr: ${stderr}`);
        }

        console.log(`stdout: ${stdout}`);
        const prediction = stdout.trim(); // Assuming the prediction is printed in stdout

        res.json({ prediction });
      });
    })
    .catch(err => {
      console.error('Error saving data to CSV:', err);
      res.status(500).send('Error saving data');
    });
});

app.listen(port, () => {
  console.log(`Server running on http://localhost:${port}`);
});
