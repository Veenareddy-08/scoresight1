import streamlit as st

# =========================
# Custom CSS Styling
# =========================
st.markdown("""
    <style>
    .stApp {
        background:
            linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)),
            url('https://www.shutterstock.com/shutterstock/photos/2645885355/display_1500/stock-vector-soccer-football-player-male-and-female-silhouette-outlines-men-and-women-group-2645885355.jpg');
        background-size: cover;
        background-position: center;
        color: white;
        font-family: 'Segoe UI';
    }

    .title-style {
        text-align: center;
        color: #ffeb3b;
        font-size: 45px;
        font-weight: 900;
        text-shadow: 2px 2px 8px black;
        margin-top: 20px;
    }

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
        transition: 0.3s ease;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.4);
    }

    .stButton > button:hover {
        transform: scale(1.07);
        background: linear-gradient(135deg, #ffffff, #ffeb3b);
    }

    .block-container {
        max-width: 750px;
        margin: auto;
        padding: 25px;
        background: rgba(0,0,0,0.45);
        border-radius: 20px;
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
if "page" not in st.session_state:
    st.session_state.page = "home"


# =========================
# Generic Input Page
# =========================
def input_page(title, fields):
    st.markdown(f"<h2>{title}</h2>", unsafe_allow_html=True)

    user_inputs = {}

    for field in fields:
        user_inputs[field] = st.text_input(field)

    if st.button("Predict"):
        st.success(f"Prediction successful with inputs: {user_inputs}")

    if st.button("⬅ Back to Home"):
        st.session_state.page = "home"


# =========================
# HOME PAGE
# =========================
if st.session_state.page == "home":
    st.markdown("<h1 class='title-style'>⚽ Football Prediction System</h1>", unsafe_allow_html=True)
    st.write("### Select a task:")

    st.button("Goals", on_click=lambda: st.session_state.update(page="goals"))
    st.button("Assist", on_click=lambda: st.session_state.update(page="assist"))
    st.button("Match Winner", on_click=lambda: st.session_state.update(page="match_winner"))
    st.button("League Points", on_click=lambda: st.session_state.update(page="league_points"))
    st.button("League Winner", on_click=lambda: st.session_state.update(page="league_winner"))


# =========================
# PAGE 1 — GOALS
# =========================
if st.session_state.page == "goals":
    goals_fields = [
        "MatchesPlayed", "Starts", "Minutes", "90sPlayed",
        "GoalsPer90", "AssistsPer90", "NonPenaltyGoalsPer90",
        "xGPer90", "xAGPer90", "npxGPer90"
    ]
    input_page("Goals Prediction", goals_fields)


# =========================
# PAGE 2 — ASSISTS
# =========================
if st.session_state.page == "assist":
    assist_fields = [
        "MatchesPlayed", "Starts", "Minutes", "90sPlayed",
        "GoalsPer90", "AssistsPer90", "NonPenaltyGoalsPer90",
        "xGPer90", "xAGPer90", "npxGPer90"
    ]
    input_page("Assist Prediction", assist_fields)


# =========================
# PAGE 3 — MATCH WINNER
# =========================
if st.session_state.page == "match_winner":
    match_fields = [
        "HTWinStreak3", "HTWinStreak5", "HTLossStreak3", "HTLossStreak5",
        "ATWinStreak3", "ATWinStreak5", "ATLossStreak3", "ATLossStreak5",
        "HTP", "ATP", "HTFormPts", "ATFormPts",
        "HTGD", "ATGD", "DiffPts", "DiffFormPts"
    ]
    input_page("Match Winner Prediction", match_fields)


# =========================
# PAGE 4 — LEAGUE POINTS
# =========================
if st.session_state.page == "league_points":
    league_points_fields = [
        "matches_played", "points_per_game", "goals_scored",
        "goals_conceded", "goal_difference", "target_total_points",
        "target_league_position", "target_champion",
        "target_top_4", "target_top_6"
    ]
    input_page("League Points Prediction", league_points_fields)


# =========================
# PAGE 5 — LEAGUE WINNER
# =========================
if st.session_state.page == "league_winner":
    league_winner_fields = [
        "played", "won", "drawn", "lost",
        "gf", "ga", "gd", "points"
    ]
    input_page("League Winner Prediction", league_winner_fields)
