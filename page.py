import streamlit as st

# Initialize session state for page navigation
if 'page' not in st.session_state:
    st.session_state.page = 'home'

# Function to show input page
def show_input_page(task_name):
    st.header(f"{task_name} Input Page")
    # Four example inputs
    input1 = st.text_input("Input 1")
    input2 = st.text_input("Input 2")
    input3 = st.text_input("Input 3")
    input4 = st.text_input("Input 4")
    
    if st.button("Submit"):
        st.success(f"Inputs submitted for {task_name}:\n{input1}, {input2}, {input3}, {input4}")
    
    if st.button("Back to Home"):
        st.session_state.page = 'home'

# Home page with buttons
if st.session_state.page == 'home':
    st.title("Football Analysis Dashboard")
    st.write("Select a task:")
    
    if st.button("Goals and Assist"):
        st.session_state.page = 'goals_assist'
    if st.button("Match Winner"):
        st.session_state.page = 'match_winner'
    if st.button("League Points"):
        st.session_state.page = 'league_points'
    if st.button("League Winner"):
        st.session_state.page = 'league_winner'

# Navigation to input pages
if st.session_state.page == 'goals_assist':
    show_input_page("Goals and Assist")
elif st.session_state.page == 'match_winner':
    show_input_page("Match Winner")
elif st.session_state.page == 'league_points':
    show_input_page("League Points")
elif st.session_state.page == 'league_winner':
    show_input_page("League Winner")
