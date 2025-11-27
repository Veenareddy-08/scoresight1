import streamlit as st

# =========================
# Custom CSS Styling
# =========================
st.markdown("""
    <style>
    
    /* Main Page Background */
    .stApp {
        background-image: linear-gradient(135deg, #1e3c72, #2a5298);
        color: white;
        font-family: 'Segoe UI', sans-serif;
    }

    /* Title Styling */
    .title-style {
        text-align: center;
        color: #ffffff;
        font-size: 40px;
        font-weight: 800;
        padding-bottom: 10px;
    }

    /* Button Styling */
    .stButton > button {
        width: 100%;
        border-radius: 12px;
        background-color: #ffffff;
        color: #2a5298;
        padding: 12px;
        font-size: 18px;
        font-weight: bold;
        transition: 0.3s ease-in-out;
        border: none;
    }

    .stButton > button:hover {
        background-color: #ffcc00;
        color: black;
        transform: scale(1.05);
    }

    /* Input Box Styling */
    .stTextInput > div > div > input {
        background-color: #ffffff;
        color: #000000;
        border-radius: 8px;
        padding: 10px;
        font-size: 16px;
    }

    /* Header Styling */
    h1, h2, h3 {
        color: #ffdd57 !important;
        text-align: center;
    }

    /* Success message */
    .stSuccess {
        background-color: #00c853 !important;
        color: white !important;
    }

    </style>
""", unsafe_allow_html=True)

# =========================
# Navigation State
# =========================
if 'page' not in st.session_state:
    st.session_state.page = 'home'

# =========================
# Input Page Function
# =========================
def show_input_page(task_name):
    st.markdown(f"<h2>{task_name} Input Page</h2>", unsafe_allow_html=True)

    input1 = st.text_input("Input 1")
    input2 = st.text_input("Input 2")
    input3 = st.text_input("Input 3")
    input4 = st.text_input("Input 4")
    
    if st.button("Submit"):
        st.success(f"Inputs submitted for {task_name}: {input1}, {input2}, {input3}, {input4}")
    
    if st.button("⬅ Back to Home"):
        st.session_state.page = 'home'

# =========================
# Home Page
# =========================
if st.session_state.page == 'home':
    st.markdown("<h1 class='title-style'>⚽ Predicting Next Match Winner</h1>", unsafe_allow_html=True)
    st.write("### Select a task:")

    st.button("Goals and Assist", on_click=lambda: st.session_state.update(page="goals_assist"))
    st.button("Match Winner", on_click=lambda: st.session_state.update(page="match_winner"))
    st.button("League Points", on_click=lambda: st.session_state.update(page="league_points"))
    st.button("League Winner", on_click=lambda: st.session_state.update(page="league_winner"))

# =========================
# Navigation Logic
# =========================
if st.session_state.page == 'goals_assist':
    show_input_page("Goals and Assist")
elif st.session_state.page == 'match_winner':
    show_input_page("Match Winner")
elif st.session_state.page == 'league_points':
    show_input_page("League Points")
elif st.session_state.page == 'league_winner':
    show_input_page("League Winner")
