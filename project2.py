import streamlit as st
import pickle
import numpy as np
import os

# =========================
# Custom CSS Styling
# =========================
st.markdown("""
    <style>
    /* Background Image with Overlay */
    .stApp {
        background: 
            linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)),
            url('https://www.shutterstock.com/shutterstock/photos/2645885355/display_1500/stock-vector-soccer-football-player-male-and-female-silhouette-outlines-men-and-women-group-2645885355.jpg');
        background-size: cover;
        background-position: center;
        font-family: 'Segoe UI', sans-serif;
        color: white;
    }

    /* Title Styling */
    .title-style {
        text-align: center;
        color: #ffeb3b;
        font-size: 45px;
        font-weight: 900;
        text-shadow: 2px 2px 8px black;
        margin-top: 20px;
    }

    /* Fancy Buttons */
    .stButton > button {
        width: 100%;
        border-radius: 14px;
        background: linear-gradient(135deg, #ffcc00, #ff8c00);
        color: black;
        padding: 14px;
        font-size: 19px;
        font-weight: bold;
        border: none;
        cursor: pointer;
        transition: 0.3s ease-in-out;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.4);
    }

    .stButton > button:hover {
        background: linear-gradient(135deg, #ffffff, #ffeb3b);
        transform: scale(1.07);
        box-shadow: 0px 6px 14px rgba(0,0,0,0.6);
    }

    /* Input Boxes */
    .stTextInput > div > div > input {
        background-color: #ffffffd9;
        color: #000000;
        border-radius: 10px;
        padding: 12px;
        font-size: 16px;
    }

    /* Success Message */
    .stSuccess {
        background-color: #21c25e !important;
        color: white !important;
        border-radius: 10px;
    }

    /* Center Content Box */
    .block-container {
        max-width: 650px;
        padding-top: 25px;
        margin: auto;
        background: rgba(0, 0, 0, 0.45);
        border-radius: 20px;
        padding-bottom: 30px;
    }

    h2 {
        color: #ffcd38 !important;
        text-align: center;
        text-shadow: 1px 1px 5px black;
    }
    </style>
""", unsafe_allow_html=True)

# =========================
# Load Models from modeltrain folder
# =========================
@st.cache_resource
def load_models():
    return {
        "goals_assists": pickle.load(open("modeltrain/Goals_Assists.pkl", "rb")),
        "match_winner": pickle.load(open("modeltrain/Match_Winner.pkl", "rb")),
        "league_winner": pickle.load(open("modeltrain/League_Winner_Prediction.pkl", "rb")),
        "league_points": pickle.load(open("modeltrain/League_Points_Prediction.pkl", "rb"))
    }

models = load_models()

# =========================
# Navigation State
# =========================
if 'page' not in st.session_state:
    st.session_state.page = 'home'

# =========================
# Input Page Function (with prediction)
# =========================
def show_input_page(task_name):
    st.markdown(f"<h2>{task_name} Input Page</h2>", unsafe_allow_html=True)

    input1 = st.text_input("Input 1")
    input2 = st.text_input("Input 2")
    input3 = st.text_input("Input 3")
    input4 = st.text_input("Input 4")
    
    if st.button("Predict"):
        if input1 and input2 and input3 and input4:
            try:
                data = np.array([[float(input1), float(input2), float(input3), float(input4)]])
                
                if task_name in ["Goals", "Assist"]:
                    prediction = models["goals_assists"].predict(data)[0]
                elif task_name == "Match Winner":
                    prediction = models["match_winner"].predict(data)[0]
                elif task_name == "League Points":
                    prediction = models["league_points"].predict(data)[0]
                elif task_name == "League Winner":
                    prediction = models["league_winner"].predict(data)[0]
                else:
                    prediction = "Unknown Task"

                st.success(f"Predicted {task_name}: {prediction}")
            except Exception as e:
                st.error(f"Error in prediction: {e}")
        else:
            st.error("Please fill all 4 inputs before predicting!")

    if st.button("⬅ Back to Home"):
        st.session_state.page = 'home'

# =========================
# Home Page
# =========================
if st.session_state.page == 'home':
    st.markdown("<h1 class='title-style'>⚽ Predicting Next Match Winner</h1>", unsafe_allow_html=True)
    st.write("### Select a task:")

    st.button("Goals", on_click=lambda: st.session_state.update(page="Goals"))
    st.button("Assist", on_click=lambda: st.session_state.update(page="Assist"))
    st.button("Match Winner", on_click=lambda: st.session_state.update(page="Match Winner"))
    st.button("League Points", on_click=lambda: st.session_state.update(page="League Points"))
    st.button("League Winner", on_click=lambda: st.session_state.update(page="League Winner"))

# =========================
# Navigation Logic
# =========================
if st.session_state.page == 'Goals':
    show_input_page("Goals")
elif st.session_state.page == 'Assist':
    show_input_page("Assist")
elif st.session_state.page == 'Match Winner':
    show_input_page("Match Winner")
elif st.session_state.page == 'League Points':
    show_input_page("League Points")
elif st.session_state.page == 'League Winner':
    show_input_page("League Winner")
