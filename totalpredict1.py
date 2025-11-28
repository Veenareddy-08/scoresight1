import streamlit as st
import joblib
import numpy as np

# =========================
# LOAD ALL MODELS
# =========================
goals_assists_model = joblib.load("Goals_Assists.pkl")  # same for Goals & Assist
match_winner_model = joblib.load("Match_Winner.pkl")
league_winner_model = joblib.load("League_Winner_Prediction.pkl")
league_points_model = joblib.load("League_Points_Prediction.pkl")

# =========================
# INPUT PAGE FUNCTION
# =========================
def show_input_page(task_name):
    st.markdown(f"<h2>{task_name} Input Page</h2>", unsafe_allow_html=True)

    input1 = st.text_input("Input 1")
    input2 = st.text_input("Input 2")
    input3 = st.text_input("Input 3")
    input4 = st.text_input("Input 4")

    if st.button("Predict"):
        if input1 and input2 and input3 and input4:

            # Convert user input to numeric format
            data = np.array([[float(input1), float(input2), float(input3), float(input4)]])

            # =========================
            # MODEL SELECTION
            # =========================
            if task_name == "Goals":
                prediction = goals_assists_model.predict(data)[0]

            elif task_name == "Assist":
                prediction = goals_assists_model.predict(data)[0]

            elif task_name == "Match Winner":
                prediction = match_winner_model.predict(data)[0]

            elif task_name == "League Points":
                prediction = league_points_model.predict(data)[0]

            elif task_name == "League Winner":
                prediction = league_winner_model.predict(data)[0]

            st.success(f"Predicted {task_name}: {prediction}")

        else:
            st.error("Please fill all 4 inputs before predicting!")

    if st.button("⬅ Back to Home"):
        st.session_state.page = 'home'


# =========================
# HOME PAGE BUTTONS
# =========================
if 'page' not in st.session_state:
    st.session_state.page = 'home'

if st.session_state.page == 'home':
    st.write("### Select a task:")
    st.button("Goals", on_click=lambda: st.session_state.update(page="goals"))
    st.button("Assist", on_click=lambda: st.session_state.update(page="assist"))
    st.button("Match Winner", on_click=lambda: st.session_state.update(page="match_winner"))
    st.button("League Points", on_click=lambda: st.session_state.update(page="league_points"))
    st.button("League Winner", on_click=lambda: st.session_state.update(page="league_winner"))

# =========================
# PAGE NAVIGATION LOGIC
# =========================
if st.session_state.page == 'goals':
    show_input_page("Goals")
elif st.session_state.page == 'assist':
    show_input_page("Assist")
elif st.session_state.page == 'match_winner':
    show_input_page("Match Winner")
elif st.session_state.page == 'league_points':
    show_input_page("League Points")
elif st.session_state.page == 'league_winner':
    show_input_page("League Winner")
