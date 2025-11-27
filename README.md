💧 AgroTechz: AI-Powered Soil Moisture Predictor

🎯 Project Overview

This project implements a machine learning model to predict the Average Soil Moisture Level (at 15cm) based on geographical, temporal, and related soil moisture parameters. The application is built using Python Flask for the backend, providing a clean, user-friendly web interface for real-time inference.

Prediction Target

Output: Average Soilmoisture Level (at 15cm)

✨ Key Features

Feature

Description

Status

Prediction Interface

A responsive web form to input all 6 required features.

✅ Complete

Dynamic Dropdowns

State selection automatically filters and populates the District dropdown.

✅ Complete

Feature Engineering

Converts human-readable Date (DD-MM-YYYY) into the Unix Timestamp feature required by the model.

✅ Complete

Data Visualization

A separate dashboard route displays historical time-series data from the input CSV.

✅ Complete

⚙️ Model Requirements (The 6 Features)

The trained model expects exactly 6 input features in a specific order for correct prediction:

No.

Feature Name

Type

Notes

1

Date

Numeric (Unix Timestamp)

Automatically converted from DD-MM-YYYY input.

2

State

Encoded

Handled by le_state.pkl.

3

District

Encoded

Handled by le_district.pkl.

4

Average SoilMoisture Volume (15cm)

Float

User input.

5

Aggregate Soilmoisture Percentage (15cm)

Float

User input.

6

Volume Soilmoisture Percentage (15cm)

Float

User input.

🚀 Setup and Run Locally

Follow these instructions to get a copy of the project running on your local machine.

Prerequisites

Python 3.x installed.

Git installed.

Model and Data Files: Ensure you have the following large files locally, as they are ignored by Git:

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

Access the UI:
Open your web browser and navigate to:

[http://127.0.0.1:5000/](http://127.0.0.1:5000/)


📂 Project Structure

File/Folder

Description

app.py

Main Flask application. Handles routing, data loading, preprocessing, and model inference.

templates/

Contains index.html (prediction form) and dashboard.html.

static/

Contains styles.css (for styling) and dependent.js (for dynamic dropdowns).

le_state.pkl

Saved scikit-learn LabelEncoder for State names.

le_district.pkl

Saved scikit-learn LabelEncoder for District names.

.gitignore

Excludes large files (*.pkl, *.csv) and virtual environments (venv/) from version control.
