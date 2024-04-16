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

# ========= HOME TAB =========
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

# ========= UPLOAD TAB =========
if selected == "Upload CSV":
    st.title("Upload CSV File")
    st.markdown('''
    ####
    To get started, select the CSV file you want to upload.
    Once uploaded, you can go ahead with the predictions and download the updated dataset from the 'Download' tab.
    ''')
    st.divider()

    with st.form("my_form"):
        batchName = st.text_input("Batch Name", placeholder="Name of batch here")
        if not batchName:  # Check if batchName is empty
            st.error("Please enter a batch name")

        st.divider()

        uploaded_file = st.file_uploader("Choose a CSV File 📂", type=['csv'])

        submitted = st.form_submit_button("Submit")
        if uploaded_file is not None and submitted:
            if batchName:
                st.success(f"File uploaded for batch '{batchName}'")
            else:
                st.error("Please enter a batch name before submitting")

        # Display a message if no file is uploaded
        if uploaded_file is None:
            st.warning("Please upload a file")


# ========= ANALYSIS TAB =========
if selected == "Analysis":
    st.title("Analysis Tab")

# ========= DOWNLOAD TAB =========
if selected == "Download CSV":
    st.title("This is the download tab")

# ========= CONTRIBUTORS =========
if selected == "Contributors":
    st.title("About Us ⚡")
    st.header("Team HardCoders 🦾")

    col1, col2 = st.columns(2)
    with col1:
        st.image("A-pfp.png")
        st.subheader("1️⃣ Abhijit Mandal")
        st.markdown('''
            * **`Github`** ⭐  
                https://github.com/abhiiiman
            * **`Linkedin`**  🔗 
                https://linkedin.com/in/abhiiiman
            * **`Portfolio`** 🌐
                https://abhiiiman.github.io/Abhijit-Mandal
        ''')

    with col2:
        st.image("D-pfp.png")
        st.subheader("2️⃣ Divyanshi")
        st.markdown('''
            * **`Github`** ⭐
                https://github.com/Divvyanshiii
            * **`Linkedin`**  🔗 
                https://linkedin.com/in/divyanshi-shrivastav
        ''')
