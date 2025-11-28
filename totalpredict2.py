import streamlit as st
import pickle
import numpy as np

# =========================
# Custom CSS Styling
# =========================
st.markdown("""
    <style>
    
    /* Background Image with Overlay */
    .stApp {
        background: 
            linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)),
            url('https://www.shutterstock.com/image-photo/soccer-ball-goal-net-stadium-600nw-2348277651.jpg');
        background-size: cover;
        background-position: center;
        color: white;
        font-family: 'Segoe UI', sans-serif;
    }

    /* Title Styling */
    h1, h2, h3 {
        color: #FFD700;
        text-align: center;
        font-weight: bold;
    }

    /* Sidebar Styling */
    .css-1d391kg {
        background-color: rgba(0, 0, 0, 0.7) !important;
        color: white !important;
    }

    </style>
""", unsafe_allow_html=True)

# =========================
# Load Models
# =========================
@st.cache_resource
def load_models():
    models = {
        "goals_assists": pickle.load(open("modeltrain/Goals_Assists.pkl", "rb")),
        "match_winner": pickle.load(open("modeltrain/Match_Winner.pkl", "rb")),
        "league_winner": pickle.load(open("modeltrain/League_Winner_Prediction.pkl", "rb")),
        "league_points": pickle.load(open("modeltrain/League_Points_Prediction.pkl", "rb")),
    }
    return models

models = load_models()

# =========================
# Navigation
# =========================
st.title("⚽ Football Prediction System")

choice = st.selectbox(
    "Select Prediction Type",
    ("-- Select --", "Match Winner", "League Winner", "Goals & Assists", "League Points")
)

# =========================
# 1️⃣ Match Winner Page
# =========================
if choice == "Match Winner":
    st.header("🏆 Match Winner Prediction")

    HTGS = st.number_input("Home Team Goals Scored", min_value=0)
    ATGS = st.number_input("Away Team Goals Scored", min_value=0)
    HTP = st.number_input("Home Team Points", min_value=0)
    ATP = st.number_input("Away Team Points", min_value=0)

    if st.button("Predict Match Winner"):
        data = np.array([[HTGS, ATGS, HTP, ATP]])
