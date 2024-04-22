import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import plotly.express as px
import pickle
import plotly.graph_objects as go

hide_st_style = """
                <style>
                #MainMenu {visibility : hidden;}
                footer {visibility : hidden;}
                header {visibility : hidden;}
                </style>
                """

# default data
batch = "2021-2025"
dataframe = pd.read_csv("collegePlacementData.csv")

st.set_page_config(
    page_title="SMART",
    page_icon="memo",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.linkedin.com/in/abhiiiman',
        'Report a bug': "https://www.github.com/abhiiiman",
        'About': "## A 'Student Performance and Placement Prediction Tool' by Abhijit Mandal & Divyanshi"
    }
)

#remove all the default streamlit configs here
st.markdown(hide_st_style, unsafe_allow_html=True)

with st.sidebar:
    selected = option_menu(
        menu_title = "S.M.A.R.T",
        options = ["Home", "Upload CSV", "Analysis", "Predictions", "Performance", "Download CSV", "Settings", "Contributors"],
        icons = ["house", "upload", "graph-up", "magic", "speedometer", "file-earmark-arrow-down", "gear", "people"],
        menu_icon= "robot",
        default_index = 0,
    )

# ========= HOME TAB =========
if selected == "Home":
    col1, col2 = st.columns([2, 1])
    with col1:
        st.title('S.M.A.R.T :rocket:')
        st.header("Student Management 🏠 And")
        st.header("Recruitment Tool 🔮")
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
        
        st.markdown("#### `Get Started Now!`")

    with col2:
        st.image("home_tab_pic.png")

# ========= UPLOAD TAB =========
if selected == "Upload CSV":
    col1, col2 = st.columns([2, 1])
    with col1:
        st.title("Upload CSV File 🗃️")
        st.markdown("#### To get started, select the CSV file you want to upload.")
        st.markdown("Once uploaded, you can go ahead with the Analysis and Predictions then download the updated dataset from the <span style = 'color:yellow'>_Download_</span> tab.", unsafe_allow_html=True)

        with st.form("my_form"):
            batchName = st.text_input("Batch Name", placeholder="Name of batch here")

            st.divider()

            uploaded_file = st.file_uploader("Choose a CSV File 📂", type=['csv'])
            submit_button = st.form_submit_button("Submit Dataset")

            if uploaded_file:
                if batchName:
                    st.balloons()
                    st.success(f"File uploaded Successfully 🎉")
                    raw_data = pd.read_csv(uploaded_file)
                    # st.header(f"{batchName} Batch Data")
                    # st.write(raw_data)
                else:
                    st.warning("Please enter a batch name before submitting")
            else:
                st.warning("Please upload a file")
    with col2:
        st.image("upload_tab_pic.png")

# ========= ANALYSIS TAB =========
if selected == "Analysis":
    col1, col2 = st.columns([2, 1])
    with col1:
        st.balloons()
        st.title("Data Analysis 📊")
        st.header(f"{batch} Batch Data")
        st.write(dataframe)

        st.divider()
    
    with col2:
        st.image("Analysis_tab_pic.png")

    # Plotting  the graph so that we can visualize the output with respect to major features  
    st.subheader("Visualization of Internships VS Placement")
    figure1 = px.scatter(dataframe, x="CGPA", y="Internships", color="PlacedOrNot", hover_data=['CGPA'])
    st.plotly_chart(figure1)

    st.divider()

    # Plotting Histogram for the count of place and not placed.
    st.subheader("Count of Placed VS Not Placed")
    figure2 = px.histogram(dataframe, x='PlacedOrNot', color='PlacedOrNot', barmode='group')
    st.plotly_chart(figure2)

    st.divider()

    # Pie Chart: Percentage pie chart of Placed or Not Placed.
    st.subheader("Placed VS Not Placed %")
    figure3 = px.pie(dataframe, values=dataframe['PlacedOrNot'].value_counts().values, names=dataframe['PlacedOrNot'].value_counts().index, title='Placed Vs Not Placed')  
    st.plotly_chart(figure3)

    st.divider()

    # Printing the Age of the youngest and Eldest student who is placed  
    st.markdown(f"### Max Age of Placed Person: `{dataframe[(dataframe['Age'] == dataframe['Age'].max()) & (dataframe['PlacedOrNot']==1)]['Age'].values[0]}`")  
    st.write(f"### Min Age of Placed Person: `{dataframe[(dataframe['Age'] == dataframe['Age'].min()) & (dataframe['PlacedOrNot']==1)]['Age'].values[0]}`")

    st.divider()

    # Printing the Maximum and the Minimum number of internships done by the student who is placed.   
    # We will also print the Maximum and Minimum number of students who did the max internship and the minimum number of internships.  
    st.markdown(f"### Max Internships Done by the Placed Student: `{dataframe[(dataframe['Internships'] == dataframe['Internships'].max()) & (dataframe['PlacedOrNot']==1)]['Internships'].values[0]}`")  
    st.markdown(f"### No of students who did max Internships and are placed: `{dataframe[(dataframe['Internships'] == dataframe['Internships'].max()) & (dataframe['PlacedOrNot']==1)]['Internships'].value_counts().values[0]}`")  
    
    st.markdown(f"### Min Internships Done by the Placed Person: `{dataframe[(dataframe['Internships'] == dataframe['Internships'].min()) & (dataframe['PlacedOrNot']==1)]['Internships'].values[0]}`")  
    st.markdown(f"### No of students who did min Internships and are placed: `{dataframe[(dataframe['Internships'] == dataframe['Internships'].min()) & (dataframe['PlacedOrNot']==1)]['Internships'].value_counts().values[0]}`")

    st.divider()

    # Printing the Maximum and Minimum number of CGPA obtained by the student who is placed.  
    # We will also print the Maximum and the Minimum number of students who got the max CGPA and minimum CGPA who are placed.  
  
    st.markdown(f"### Max CGPA of Placed Student: `{dataframe[(dataframe['CGPA'] == dataframe['CGPA'].max()) & (dataframe['PlacedOrNot']==1)]['CGPA'].values[0]}`")  
    st.markdown(f"### No of students has max CGPA and are placed: `{dataframe[(dataframe['CGPA'] == dataframe['CGPA'].max()) & (dataframe['PlacedOrNot']==1)]['CGPA'].value_counts().values[0]}`")  
    
    st.markdown(f"### Min CGPA of Placed Person: `{dataframe[(dataframe['CGPA'] == dataframe['CGPA'].min()) & (dataframe['PlacedOrNot']==1)]['CGPA'].values[0]}`")  
    st.markdown(f"### No of students has min CGPA and are placed: `{dataframe[(dataframe['CGPA'] == dataframe['CGPA'].min()) & (dataframe['PlacedOrNot']==1)]['CGPA'].value_counts().values[0]}`")

    st.divider()

    # box plots for different features here
    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("Box Plot - CGPA")
        figure = px.box(dataframe, y='CGPA')
        st.plotly_chart(figure, use_container_width=True, height=400, width=300)
        
    with col2:
        st.subheader("Box Plot - Age")
        figure = px.box(dataframe, y='Age')
        st.plotly_chart(figure, use_container_width=True, height=400, width=300)

    with col3:
        st.subheader("Box Plot - Internship, CGPA, Age")
        figure = px.box(dataframe, y=['Internships', 'CGPA', 'Age'])
        st.plotly_chart(figure, use_container_width=True, height=400, width=300)

# ========= PREDICTION TAB =======
if selected == "Predictions":
    col1, col2 = st.columns([2, 1])
    with col1:
        st.title("Placement Prediction ⚡")
        st.subheader("Provide the inputs below 👇🏻")
        st.divider()
        st.markdown("##### _Here we will use <span style='color:yellow'>Random Forest 🤖</span> Machine Learning Algorithm to create our Model to predict the Placement of Students_.", unsafe_allow_html=True)
        st.markdown("##### _You just need to provide the individual student data to get started and predict their placement probability using our <span style = 'color:yellow'>well trained Model right here</span>_.", unsafe_allow_html=True)
    with col2:
        st.image("prediction_tab_pic.png")

    st.divider()

    col1, col2 = st.columns(2)

    with col1:
        # Get user input for Age
        age = st.slider('Enter the Age 👇🏻', min_value=18, max_value=30, step=1)
        # Get user input for Internships
        internships = st.slider('Enter Number of Internships 👇🏻', min_value=0, max_value=10, step=1)
        # Get user input for CGPA
        cgpa = st.slider('Enter the CGPA 👇🏻', min_value=0.0, max_value=10.0, step=0.1)
        predict_button = st.button("Predict the Placement ⚡")

    with col2:
        # Get user input for Gender
        gender = st.selectbox('Choose Gender 🧑🏻‍🦱👧🏻', ['Male', 'Female'])
        # Get user input for Stream
        stream = st.selectbox('Choose Stream 🎓', ['Electronics And Communication', 'Computer Science', 'Information Technology', 'Mechanical', 'Electrical', 'Civil'])
        # Get user input for Hostel
        hostel = st.selectbox('Hostel 🏡', ['Yes', 'No'])
        # Get user input for History of Backlogs
        backlogs = st.selectbox("History of Backlogs 👇🏻", ['Yes', "No"])
    
    # encoding the variables here.

    #gender
    if gender == 'Male': gender_encoded = 1
    else: gender_encoded = 0

    # stream
    if stream == 'Electronics And Communication': stream_encoded = 1
    elif stream == 'Computer Science': stream_encoded = 2
    elif stream == 'Information Technology': stream_encoded = 3
    elif stream == 'Mechanical': stream_encoded = 4
    elif stream == 'Electrical': stream_encoded = 5
    elif stream == 'Civil': stream_encoded = 6
    else: 'Invalid Stream Selected'

    # Hostel
    hostel_encoded = 1 if hostel == 'Yes' else 0

    # backlog history
    backlogs_encoded = 1 if backlogs == 'Yes' else 0

    # Check if the Predict Placement button is clicked
    if predict_button:

        st.balloons()

        # Prepare the user input as a dataframe
        user_data = {
            'Age': [age],
            'Gender': [gender],
            'Stream': [stream],
            'Internships': [internships],
            'CGPA': [cgpa],
            'Hostel': [hostel],
            'HistoryOfBacklogs': [backlogs]
        }
        user_df = pd.DataFrame(user_data)
        st.divider()
        st.markdown("* ## Input Dataframe ⬇️")
        st.write(user_df)

        # Make predictions using the loaded model
        model = pickle.load(open("Placement_Model", 'rb'))

        # Display the prediction result
        prediction = model.predict([[age, gender_encoded, stream_encoded, internships, cgpa, hostel_encoded, backlogs_encoded]])
        st.markdown("* ## Prediction Result ✅")
        if prediction == 1:
            st.markdown("### <span style='color:lightgreen'>Placed 🎉</span>", unsafe_allow_html=True)
        else:
            st.markdown("### <span style='color:red'>Not Placed 😢</span>", unsafe_allow_html=True)


    st.divider()

    st.markdown("## Prediction using <span style='color:yellow'>_Random Forest Classifier_ 🦾</span>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("* #### Best Accuracy : <span style='color:yellow'>_83%_ 🦾</span>", unsafe_allow_html=True)
        st.markdown("* #### With Cross Validation : <span style='color:yellow'>_82.57%_ ⬆️</span>", unsafe_allow_html=True)
        st.markdown("* #### Precision Score : <span style='color:yellow'>_94.08%_ ⚡</span>", unsafe_allow_html=True)

    with col2:
        st.markdown("* #### F1 Score : <span style='color:yellow'>_81.74%_ 🦾</span>", unsafe_allow_html=True)
        st.markdown("* #### Without Cross Validation : <span style='color:yellow'>_81.11%_ ⬇️</span>", unsafe_allow_html=True)
        st.markdown("* #### Recall Score : <span style='color:yellow'>_72.27%_ ⚡</span>", unsafe_allow_html=True)

# ========= PERFORMANCE TAB ======
if selected == "Performance":
    col1, col2 = st.columns([2, 1])
    with col1:
        st.title("Student Performance Analysis⚡")
        st.subheader("Provide the inputs below 👇🏻")
        st.divider()
        st.markdown("_<font size = '4'>In this section, we delve into the comprehensive analysis of student performance throughout their academic journey. By examining semester-wise progress and performance metrics, we gain insights into their academic trajectory, identifying areas of strength and areas needing improvement. This detailed analysis aids in providing personalized guidance and support for each student's educational success.</font>_", unsafe_allow_html=True)
    with col2:
        st.image("Student_Performance_Pic.png")
    
    st.divider()

    col1, col2 = st.columns([2, 2])

    with col2:
        st.subheader("Input Dataset 👇🏻")
        dataset_file = st.file_uploader("Enter that Batch's Dataset here")

    with col1:
        st.subheader("Input Student Batch 👇🏻")
        batch_year = st.text_input("Enter the Batch Year here", value="2021-2025")
        if dataset_file:
            with st.expander("Preview Uploaded Dataset"):
                dataframe = pd.read_excel(dataset_file)
                st.dataframe(dataframe)
    
    st.divider()

    if dataset_file:
        global selected_student

        # perform performance analysis
        st.header("SGPA Performance Analysis 💯")

        # Create a list of options for the selectbox
        options = ["Select Student"] + list(dataframe['Name'].unique())

        # Create the selectbox with the list of options
        selected_student = st.selectbox("Select a Student", options)

        # Remove the default value if "Select Student" is selected
        if selected_student == "Select Student":
            selected_student = None

        # button to start the performance analysis for that selected student.
        performance_button = st.button(f"Perform Analysis for {selected_student}")
        if performance_button:
            if selected_student is not None:

                # Filter the DataFrame for the selected student
                student_data = dataframe[dataframe["Name"] == selected_student]
                
                # perform the analysis here
                # 1. SGPA analysis
                
                # Prepare the data for plotting
                semesters = student_data.columns[2:7]  # Exclude the 'Name' and 'Roll no' column
                sgpa_marks = student_data.values.flatten()[2:7]  # Flatten the data and exclude the 'Name' column

                # Plot the chart
                fig = go.Figure(data=go.Scatter(x=semesters, y=sgpa_marks, mode='lines+markers'))
                # Add annotations for each data point
                for semester, sgpa in zip(semesters, sgpa_marks):
                    fig.add_annotation(
                        x=semester,
                        y=sgpa,
                        text=f"SGPA: {sgpa}",
                        showarrow=True,
                        arrowhead=1,
                        ax=0,
                        ay=-40
                    )
                fig.update_layout(title=f"1. Trend of SGPA for {selected_student}", xaxis_title='Semester', yaxis_title='SGPA')
                st.plotly_chart(fig)

            else:
                st.warning("Select a Student first ⚠️")

        # 2. multi SGPA analysis.
        # Select multiple students from the dropdown
        st.header("Multiple SGPA Performance Analysis 📑")
        selected_students = st.multiselect("Select Students", dataframe["Name"])
        # Filter the DataFrame for the selected students
        student_data = dataframe[dataframe["Name"].isin(selected_students)]

        # button to start the performance analysis for that selected student.
        multi_performance_button = st.button(f"Perform Analysis for the selected students")

        if multi_performance_button:
            # print(selected_students)
            if selected_students:
                # Plot the chart
                fig = go.Figure()

                # Plot SGPA trend for each selected student
                for index, row in student_data.iterrows():
                    semesters = row.index[2:7]  # Exclude the 'Name' column
                    sgpa_marks = row.values[2:7]  # Exclude the 'Name' column

                    # Add a line for the current student
                    fig.add_trace(go.Scatter(x=semesters, y=sgpa_marks, mode='lines+markers', name=row["Name"]))

                fig.update_layout(title="2. Trend of SGPA for Selected Students", xaxis_title='Semester', yaxis_title='SGPA')
                st.plotly_chart(fig)

            else:
                st.warning("Select Multiple Students first ⚠️")
        
        # perform attendance analysis
        if performance_button:
            if selected_student is not None:
                # Filter the DataFrame for the selected student
                student_data = dataframe[dataframe["Name"] == selected_student]
                st.header("Attendance Analysis 🙋🏻")
                # Prepare the data for plotting
                subjects = student_data.columns[7:12] # exctracting the subjects here
                attendances = student_data.values.flatten()[7:12]  # Flatten the data and exclude other columns
                # Plot the chart
                fig = go.Figure(data=go.Scatter(x=subjects, y=attendances, mode='lines+markers'))
                # Add annotations for each data point
                for subject, attendance in zip(subjects, attendances):
                    fig.add_annotation(
                        x=subject,
                        y=attendance,
                        text=f"attendance: {attendance}",
                        showarrow=True,
                        arrowhead=1,
                        ax=0,
                        ay=-40
                    )
                fig.update_layout(title=f"3.1 Trend of attendance for {selected_student}", xaxis_title='Subjects', yaxis_title='attendance')
                st.plotly_chart(fig)

                col1, col2 = st.columns([2, 2])
                with col1:
                    # Plot bar chart
                    fig_bar = go.Figure(data=[go.Bar(x=subjects, y=attendances)])
                    fig_bar.update_layout(title=f"3.2 Trend of Attendance for {selected_student}", xaxis_title='Subjects', yaxis_title='Attendance')
                    st.plotly_chart(fig_bar)
                
                with col2:
                    # Plot pie chart
                    fig_pie = go.Figure(data=[go.Pie(labels=subjects, values=attendances)])
                    fig_pie.update_traces(hoverinfo='label+percent', textinfo='value', textfont_size=20, marker=dict(colors=px.colors.qualitative.Pastel1, line=dict(color='#000000', width=2)))
                    fig_pie.update_layout(title=f"3.3 Trend of Attendance Distribution for {selected_student}")
                    st.plotly_chart(fig_pie)

        # some other student details 
        if performance_button:
            if selected_student is not None:
                st.divider()
                st.markdown(f"## Some More Details about <span style = 'color:yellow'>{selected_student}</span>", unsafe_allow_html=True)

                # init the vars here.
                internship_status = False
                UFM_status = False
                reappear_status = False

                # fetching the details here.
                internship_data = student_data["Internship Status"].iloc[0]
                if internship_data == 1: internship_status = True

                UFM_data = student_data["UFM"].iloc[0]
                if UFM_data == 1: UFM_status = True

                reappear_data = student_data["ReAppear"].iloc[0]
                if reappear_data == 1: reappear_status = True

                # other details
                st.markdown(f'''
                    * #### Internship Status : `{internship_status}`
                    * #### UFM Status : `{UFM_status}`
                    * #### Reappear History : `{reappear_status}`
                    * #### Backlog History : `{reappear_status}`
                ''')

# ========= SETTINGS TAB =========
if selected == "Settings":
    col1, col2 = st.columns([2, 2])
    with col1:
        st.title("App Settings ⚙️")
        st.divider()

        st.subheader("1. App Appearance 🎨")
        theme = st.radio("Select Theme:", options=["Dark", "Light"], index=0)
        st.divider()

        st.subheader("2. App Features ⚡")
        show_3d_images = st.checkbox("Show 3D Images 🖼️", value=True)
        enable_animations = st.checkbox("Enable Animations 🫏", value=True)
        st.divider()
    with col2:
        st.image("AppSettings.png")

    st.markdown("### Bug Report 🪲")
    bug_report = st.text_area("Please describe the issue or report a bug:")
    uploaded_file = st.file_uploader("Attach Screenshot (optional):", type=["png", "jpg"])
    if uploaded_file is not None:
        st.markdown("**<span style = 'color:lightgreen'>Screenshot Attached Successfully 👍🏻</span>**", unsafe_allow_html=True)
        with st.expander("Preview Attached Screenshot"):
            st.image(uploaded_file)
    send_button = st.button("Send Report ✈️")
    if send_button:
        st.markdown("<span style = 'color:lightgreen'>Report Sent Successfully, We'll get back to you super soon ⚡</span>", unsafe_allow_html=True)
        st.markdown("## <span style = 'color:white'>Thank You 💖</span>", unsafe_allow_html=True)
        st.markdown("#### <span style = 'color:yellow'>Team HardCoders 🦾</span>", unsafe_allow_html=True)

# ========= DOWNLOAD TAB =========
if selected == "Download CSV":
    col1, col2 = st.columns([2, 1])
    with col1:
        st.title("Download Batch Predictions 📂")
        st.subheader("Provide the Batch Dataset below 👇🏻")
        st.divider()

        uploaded_file = st.file_uploader("Upload your Batch Dataset file here")
        if uploaded_file:
            with st.expander("Click to Preview Uploaded Dataset"):
                batch_df = pd.read_csv(uploaded_file)
                st.dataframe(batch_df)

        predict_button = st.button("Make Placement Predictions ⚡")
        if predict_button:
            if uploaded_file:
                # Make predictions using the loaded model
                model = pickle.load(open("Placement_Model", 'rb'))

                # Predict placement for each student and store the predictions in a new column
                placement_predictions = []

                def encode_stream(stream):
                    if stream == 'Electronics And Communication': return 1
                    elif stream == 'Computer Science': return 2
                    elif stream == 'Information Technology': return 3
                    elif stream == 'Mechanical': return 4
                    elif stream == 'Electrical': return 5
                    elif stream == 'Civil': return 6
                    else: 'Invalid Stream Selected'

                with st.spinner("Predictions are in Progress, Please Wait..."):
                    # Initialize progress bar
                    progress_bar = st.progress(0)

                    # Iterate over each row in the dataframe
                    for index, row in batch_df.iterrows():
                        # Extract features for the student
                        age = row['Age']
                        gender_encoded = 1 if row['Gender'] == 'Male' else 0
                        stream_encoded = encode_stream(row['Stream'])  # Define this function to encode the stream
                        internships = row['Internships']
                        cgpa = row['CGPA']
                        hostel_encoded = 1 if row['Hostel'] == 'Yes' else 0
                        backlogs_encoded = 1 if row['HistoryOfBacklogs'] == 'Yes' else 0

                        # Make prediction for the student
                        prediction = model.predict([[age, gender_encoded, stream_encoded, internships, cgpa, hostel_encoded, backlogs_encoded]])
                        placement_predictions.append(prediction[0])

                        # Update progress bar
                        progress_bar.progress((index + 1) / len(batch_df))

                new_df = pd.read_excel("Student Dataset.xlsx")

                # Add the placement predictions to a new column in the dataframe
                new_df['PlacementPrediction'] = placement_predictions

                # Save the updated dataframe
                # batch_df.to_csv("updated_dataframe.csv", index=False)

                # Display a success message
                st.balloons()
                st.success("Predictions Completed 🎉")

                # Provide a button to download the updated dataframe
                st.download_button(
                    label="Download Updated DataFrame",
                    data=new_df.to_csv().encode('utf-8'),
                    file_name="Placement_Prediction.csv",
                    mime="text/csv"
                )
                with st.expander("Click to Preview Prediction Dataset"):
                    st.dataframe(new_df)

            else:
                st.warning("Please Upload your Dataset first ⚠️")

    with col2:
        st.image("Download_Tab_Pic.png")


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
