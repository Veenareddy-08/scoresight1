import streamlit as st

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
        margin-top: 10px;
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

    h2 {
        color: #ffcd38 !important;
        text-align: center;
        text-shadow: 1px 1px 5px black;
    }

    </style>
""", unsafe_allow_html=True)


# =========================
# Navigation State
# =========================
if 'page' not in st.session_state:
    st.session_state.page = 'home'


# =========================
# Goals Page Function
# =========================
def show_goals_page():
    st.markdown("<h2>🎯 Goals Prediction</h2>", unsafe_allow_html=True)

    features = [
        'Position', 'Age', 'MatchesPlayed', 'Starts', 'Minutes', '90sPlayed',
        'GoalsPer90', 'AssistsPer90', 'NonPenaltyGoalsPer90',
        'xGPer90', 'xAGPer90', 'npxGPer90'
    ]

    user_inputs = {}

    for feature in features:
        user_inputs[feature] = st.text_input(f"{feature}")

    st.write("")

    # Predict button
    if st.button("🔮 Predict Goals"):
        st.success("Prediction complete! (Model not connected yet)")

    # Back button
    if st.button("⬅ Back to Home"):
        st.session_state.page = "home"


# =========================
# Home Page
# =========================
if st.session_state.page == 'home':
    st.markdown("<h1 class='title-style'>⚽ Predicting Next Match Winner</h1>", unsafe_allow_html=True)
    st.write("### Select a task:")

    st.button("Goals", on_click=lambda: st.session_state.update(page="goals"))
    st.button("Assist", on_click=lambda: st.session_state.update(page="Assist"))
    st.button("Match Winner", on_click=lambda: st.session_state.update(page="match_winner"))
    st.button("League Points", on_click=lambda: st.session_state.update(page="league_points"))
    st.button("League Winner", on_click=lambda: st.session_state.update(page="league_winner"))


# =========================
# Navigation Logic
# =========================
if st.session_state.page == 'goals':
    show_goals_page()

elif st.session_state.page == 'Assist':
    st.write("Assist Page Coming Soon...")

elif st.session_state.page == 'match_winner':
    st.write("Match Winner Page Coming Soon...")

elif st.session_state.page == 'league_points':
    st.write("League Points Page Coming Soon...")

elif st.session_state.page == 'league_winner':
    st.write("League Winner Page Coming Soon...")
