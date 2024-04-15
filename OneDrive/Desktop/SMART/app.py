import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(
    page_title="SMART",
    page_icon="memo",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.linkedin.com/in/divyanshi-shrivastav',
        'Report a bug': "https://www.github.com/Divvyanshii",
        'About': "## A 'Student Performance and Placement Prediction Tool' by Divyanshi & Abhijit Mandal"
    }
)

with st.sidebar:
    selected = option_menu(
        menu_title = "S.M.A.R.T",
        options = ["Home", "Upload CSV", "Analysis", "Download CSV", "Settings", "Contributors"],
        icons = ["house", "upload", "graph-up", "file-earmark-arrow-down", "gear", "people"],
        menu_icon= "robot",
        default_index = 0,
    )

if selected == "Home":
    st.title('S.M.A.R.T :rocket:')
    st.subheader("Student Management And Recruitment Tool")
    st.divider()

    st.header("About :memo:")
    st.markdown('''
    ####
    We are thrilled to introduce you to SMART, your all-in-one solution for student
    management and recruitment needs
    providing a comprehensive platform for tracking academic progress, 
    facilitating career development, and predicting placement opportunities.
    With SMART, educational institutions can efficiently manage student data,
    track their academic performance, and streamline the recruitment process. 
    Meanwhile, students can access personalized career guidance, 
    explore job opportunities, and receive tailored recommendations
    for enhancing their employability. 
    Join us on this exciting journey as we revolutionize
    student management and recruitment with SMART!
    ''')

    st.button("Get Started")


if selected == "Upload CSV":
    st.title("This is a complete new page")



