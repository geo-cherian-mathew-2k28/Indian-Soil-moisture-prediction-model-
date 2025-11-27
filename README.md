<h1 style="font-size:50px; text-align:center;">AgroTechz: AI-Powered Soil Moisture Predictor</h1>
****Project Overview****

This project uses a machine learning model to predict the Average Soil Moisture Level (at 15cm) based on geographical, temporal, and soil parameters. The backend is built using Python Flask with a simple, user-friendly interface for real-time predictions.

Technology Stack

    Backend: Python 3.x, Flask
    Machine Learning: scikit-learn (Random Forest)
    Data Handling: pandas, joblib
    Frontend: HTML, Bootstrap, JavaScript

Prediction Target

    Output: Average Soil Moisture Level (at 15cm)

Key Features

    Responsive prediction form for 6 required features

    Dynamic dropdowns (State → District)

    Auto-conversion of date to Unix timestamp

    Dashboard for time-series soil moisture data

Model Requirements (6 Features)

    Date (Unix Timestamp)

    State (Encoded by le_state.pkl)

    District (Encoded by le_district.pkl)

    Average Soil Moisture Volume (15cm)

    Aggregate Soil Moisture Percentage (15cm)

    Volume Soil Moisture Percentage (15cm)

Setup & Run Locally
Prerequisites:

  1.Python 3.x
  2.Git
  3.Local required files:

    soil_moisture_model.pkl

    merged_soil_dataset.csv

Installation Steps

1. Clone the Repository:
   
        git clone  https://github.com/geo-cherian-mathew-2k28/Indian-Soil-moisture-prediction-model-.git
        cd Indian-Soil-moisture-prediction-model

3. Create Virtual Environment
   
        python -m venv venv

    Activate (Linux/macOS):
   
        source venv/bin/activate
   
    Activate (Windows):
   
        .\venv\Scripts\activate

4. Install Dependencies
   
         pip install Flask pandas numpy joblib scikit-learn==1.6.1

5. Run the App
   
         python app.py

Access the App

Open browser and go to:

      http://127.0.0.1:5000/

Project Structure

    app.py — Main Flask backend
    templates/ — index.html (form), dashboard.html
    static/ — styles.css, dependent.js
    le_state.pkl — Encoded state labels
    le_district.pkl — Encoded district labels
    .gitignore — Ignores large files and venv
