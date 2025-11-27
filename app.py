from flask import Flask, render_template, request, jsonify
import pandas as pd
import numpy as np
import joblib
import os
from sklearn.preprocessing import LabelEncoder
from datetime import datetime

app = Flask(__name__, static_folder="static", template_folder="templates")

BASE = os.path.dirname(os.path.abspath(__file__))

# File paths
MODEL_PATH = os.path.join(BASE, "soil_moisture_model.pkl")
CSV_PATH = os.path.join(BASE, "merged_soil_dataset.csv")
LE_STATE_PATH = os.path.join(BASE, "le_state.pkl")
LE_DISTRICT_PATH = os.path.join(BASE, "le_district.pkl")

# --- Mock Model Setup (Used if actual model fails to load) ---
class MockModel:
    def predict(self, df_row):
        if df_row.shape[1] != 6:
             raise Exception(f"Model expects 6 features, but received {df_row.shape[1]}. Check feature selection and order.")
        
        mock_result = (df_row.iloc[0, 3] + df_row.iloc[0, 4] + df_row.iloc[0, 5]) / 3
        return np.array([mock_result * 0.01]) 

# Load dataset for dropdowns & encoder reference
try:
    df = pd.read_csv(CSV_PATH)
except Exception as e:
    print(f"FATAL ERROR: Could not load the CSV file ({CSV_PATH}). Application cannot run.")
    raise e

# Column names from the raw CSV
STATE_COL = "State Name"
DIST_COL  = "DistrictName"

# --- CRITICAL FIX 1: Data Cleaning (Prevents TypeError and handles NaN) ---
df[STATE_COL] = df[STATE_COL].astype(str).str.strip()
df[DIST_COL]  = df[DIST_COL].astype(str).str.strip()


# --- CRITICAL FIX 2: Robust Model and Encoder Initialization ---

model = None
le_state = LabelEncoder()
le_district = LabelEncoder()

# 1. Load Model
try:
    model = joblib.load(MODEL_PATH)
    print(f"INFO: Successfully loaded model from {MODEL_PATH}.")
except Exception as e:
    print(f"WARNING: Failed to load actual model file. Using MockModel for predictions.")
    print(f"Details: {e}")
    model = MockModel()

# 2. Load Encoders
try:
    le_state.classes_ = joblib.load(LE_STATE_PATH).classes_
    le_district.classes_ = joblib.load(LE_DISTRICT_PATH).classes_
    print("INFO: Successfully loaded LabelEncoder classes.")
except Exception as e:
    print(f"WARNING: Failed to load encoder files. Fitting on CSV data as fallback.")
    print(f"Details: {e}")
    le_state.fit(df[STATE_COL])
    le_district.fit(df[DIST_COL])


# -----------------------------
# SAFE ENCODER FUNCTIONS
# -----------------------------
def encode_state(val):
    val = str(val).strip()
    if val in le_state.classes_:
        return le_state.transform([val])[0]
    return len(le_state.classes_) 

def encode_district(val):
    val = str(val).strip()
    if val in le_district.classes_:
        return le_district.transform([val])[0]
    return len(le_district.classes_) 

# -----------------------------
# INPUT PREPARATION (6 Features Required)
# Feature Order: [Date(TS), State(E), District(E), MoistureVolume, Agg_Pct, Volume_Pct]
# -----------------------------
def prepare_input(state, district, avg_volume, agg_pct, volume_pct, date_str):
    
    # Date to Unix Timestamp (CRITICAL: Must match training logic)
    try:
        date_obj = datetime.strptime(date_str, '%d-%m-%Y') 
        date_timestamp = int(date_obj.timestamp())
    except ValueError:
        raise ValueError("Invalid date format. Please use DD-MM-YYYY (e.g., 01-01-2020).")

    # Categorical and Numerical conversion
    enc_state = encode_state(state)
    enc_district = encode_district(district)
    
    try:
        avg_volume_val = float(avg_volume)
        agg_pct_val = float(agg_pct)
        volume_pct_val = float(volume_pct)
    except ValueError:
        raise ValueError("Non-numeric value provided for a moisture field.")

    # Create the input DataFrame - ORDER IS CRITICAL!
    feature_cols = [
        'Date', 
        'State', 
        'District', 
        'MoistureVolume', 
        'Aggregate Soilmoisture Percentage (at 15cm)',
        'Volume Soilmoisture percentage (at 15cm)'
    ]
    
    data = [[date_timestamp, enc_state, enc_district, avg_volume_val, agg_pct_val, volume_pct_val]]
    
    return pd.DataFrame(data, columns=feature_cols)

# Helper function for getting clean state lists
def get_valid_states():
    unique_states = df[STATE_COL].unique()
    return [s for s in unique_states if s.lower() != 'nan' and s.strip()]

# -----------------------------
# FLASK ROUTES
# -----------------------------
@app.route("/")
def home():
    return render_template("index.html", 
                           states=sorted(get_valid_states()))


@app.route("/get_districts/<state>")
def get_districts(state):
    # This is the route the JavaScript hits
    state = str(state).strip()
    
    # Filter the main DataFrame based on the selected state
    if state in df[STATE_COL].unique():
        districts = sorted(df[df[STATE_COL] == state][DIST_COL].unique())
        # Clean the districts list before sending to JS
        valid_districts = [d for d in districts if d.lower() != 'nan' and d.strip()]
    else:
        valid_districts = []
        
    # Return as JSON for the JavaScript fetch call
    return jsonify({"districts": valid_districts})


@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Collect 6 inputs
        state = request.form["state"]
        district = request.form["district"]
        avg_volume = request.form["avg_volume"]
        agg_pct = request.form["agg_pct"] 
        volume_pct = request.form["volume_pct"]
        date = request.form.get("date", datetime.now().strftime('%d-%m-%Y')) 

        df_row = prepare_input(
            state, 
            district, 
            avg_volume, 
            agg_pct, 
            volume_pct, 
            date
        ) 
        
        pred = float(model.predict(df_row)[0])

        return render_template("index.html",
                               states=sorted(get_valid_states()),
                               prediction_text=f"Predicted Soil Moisture LEVEL (at 15cm): {pred:.3f}")

    except Exception as e:
        return render_template("index.html",
                               states=sorted(get_valid_states()),
                               error_text=f"Prediction Error: {e}")


@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


@app.route("/dashboard/data")
def dash_data():
    try:
        df2 = df.copy()
        df2["Date"] = pd.to_datetime(df2["Date"], dayfirst=True, errors="coerce")
        target_col_name = "Volume Soilmoisture percentage (at 15cm)"
        ts = df2.groupby("Date")[target_col_name].mean().dropna()

        dates = ts.index.strftime('%Y-%m-%d').tolist()
        
        return jsonify({
            "dates": dates,
            "values": ts.values.tolist(),
            "target_col": target_col_name
        })

    except Exception as e:
        return jsonify({"error": str(e)})


if __name__ == "__main__":
    app.run(debug=True)