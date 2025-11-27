<h1 style="font-size:50px; text-align:center;">AgroTechz: AI-Powered Soil Moisture Predictor</h1>
<h2 style="font-size:50px; text-align:center;">Project Overview</h2>

This project uses a machine learning model to predict the Average Soil Moisture Level (at 15cm) based on geographical, temporal, and soil parameters. The backend is built using Python Flask with a simple, user-friendly interface for real-time predictions.

<h2 style="font-size:50px; text-align:center;">Technology Stack</h2>    

    Backend: Python 3.x, Flask
    Machine Learning: scikit-learn (Random Forest)
    Data Handling: pandas, joblib
    Frontend: HTML, Bootstrap, JavaScript

<h2 style="font-size:50px; text-align:center;">Prediction Target</h2>    

    Output: Average Soil Moisture Level (at 15cm)

<h2 style="font-size:50px; text-align:center;">Key Features</h2>    

    Responsive prediction form for 6 required features

    Dynamic dropdowns (State → District)

    Auto-conversion of date to Unix timestamp

    Dashboard for time-series soil moisture data

<h2 style="font-size:50px; text-align:center;">Model Requirements (6 Features)</h2>    

    Date (Unix Timestamp)

    State (Encoded by le_state.pkl)

    District (Encoded by le_district.pkl)

    Average Soil Moisture Volume (15cm)

    Aggregate Soil Moisture Percentage (15cm)

    Volume Soil Moisture Percentage (15cm)

<h2 style="font-size:50px; text-align:center;">Setup & Run Locally</h2>    
<h3 style="font-size:50px; text-align:center;">Prerequisites:</h3>    

  1.Python 3.x
  2.Git
  3.Local required files:

    soil_moisture_model.pkl

    merged_soil_dataset.csv

<h2 style="font-size:50px; text-align:center;">Installation Steps</h2>    

<h3 style="font-size:50px; text-align:center;">1. Clone the Repository:</h3>    
   
        git clone  https://github.com/geo-cherian-mathew-2k28/Indian-Soil-moisture-prediction-model-.git
        cd Indian-Soil-moisture-prediction-model

<h2 style="font-size:50px; text-align:center;">2. Create Virtual Environment</h2>    
   
        python -m venv venv

<h3 style="font-size:50px; text-align:center;">Activate (Linux/macOS):</h3>    
   
        source venv/bin/activate
   
<h3 style="font-size:50px; text-align:center;">Activate (Windows):</h3>    
   
        .\venv\Scripts\activate

<h2 style="font-size:50px; text-align:center;">4. Install Dependencies</h2>    
   
         pip install Flask pandas numpy joblib scikit-learn==1.6.1

<h2 style="font-size:50px; text-align:center;">5. Run the App</h2>    
   
         python app.py

<h2 style="font-size:50px; text-align:center;">Access the App</h2>    

<h3 style="font-size:50px; text-align:center;">Open browser and go to:</h3>    

      http://127.0.0.1:5000/

<h2 style="font-size:50px; text-align:center;">Project Structure</h2>    

    app.py — Main Flask backend
    templates/ — index.html (form), dashboard.html
    static/ — styles.css, dependent.js
    le_state.pkl — Encoded state labels
    le_district.pkl — Encoded district labels
    .gitignore — Ignores large files and venv
