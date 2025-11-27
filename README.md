💧 AgroTechz: AI-Powered Soil Moisture Predictor

🎯 Project Overview

This project implements a machine learning model to predict the Average Soil Moisture Level (at 15cm) based on geographical, temporal, and related soil moisture parameters. The application is built using Python Flask for the backend, providing a clean, user-friendly web interface for real-time inference.

Technology Stack

Backend: Python 3.x / Flask

Machine Learning: scikit-learn (Random Forest Regressor)

Data Handling: pandas, joblib (CSV, Pickle files)

Frontend: HTML, Bootstrap, JavaScript

Prediction Target

Output: Average Soilmoisture Level (at 15cm)

✨ Key Features

Prediction Interface: A responsive web form to input all 6 required features.

Dynamic Dropdowns: State selection automatically filters and populates the District dropdown.

Feature Engineering: Converts human-readable Date (DD-MM-YYYY) into the Unix Timestamp feature required by the model.

Data Visualization: A separate dashboard route displays historical time-series data from the input CSV.

⚙️ Model Requirements (The 6 Features)

The trained model expects exactly 6 input features in this specific order for correct prediction:

Date: Numeric (Unix Timestamp). Automatically converted from user input.

State: Encoded. Handled by le_state.pkl.

District: Encoded. Handled by le_district.pkl.

Average SoilMoisture Volume (15cm): Float. User input.

Aggregate Soilmoisture Percentage (15cm): Float. User input.

Volume Soilmoisture Percentage (15cm): Float. User input.

🚀 Setup and Run Locally

Follow these instructions to get a copy of the project running on your local machine.

Prerequisites

Python 3.x installed.

Git installed.

Model and Data Files: Ensure you have the following large files locally, as they are ignored by Git and cannot be cloned:

soil_moisture_model.pkl

merged_soil_dataset.csv

Installation Steps

Clone the Repository:

git clone [https://github.com/YOUR_GITHUB_USERNAME/YOUR_REPO_NAME.git](https://github.com/YOUR_GITHUB_USERNAME/YOUR_REPO_NAME.git)
cd YOUR_REPO_NAME


Create a Virtual Environment (Recommended):

python -m venv venv
source venv/bin/activate   # Linux/macOS
.\venv\Scripts\activate    # Windows


Install Dependencies:

# Note: Use the exact scikit-learn version used for training (e.g., 1.6.1)
pip install Flask pandas numpy joblib scikit-learn==1.6.1


Run the Application:

python app.py


The application will start on your local development server.

Access the UI: Open your web browser and navigate to the local server address. (This text uses the Blockquote syntax for a background box effect.)

Access URL: http://127.0.0.1:5000/

📂 Project Structure

app.py: Main Flask application. Handles routing, data loading, preprocessing, and model inference.

templates/: Contains index.html (prediction form) and dashboard.html.

static/: Contains styles.css (for styling) and dependent.js (for dynamic dropdowns).

le_state.pkl: Saved scikit-learn LabelEncoder for State names.

le_district.pkl: Saved scikit-learn LabelEncoder for District names.

.gitignore: Excludes large files (*.pkl, *.csv) and virtual environments (venv/) from version control.
