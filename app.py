import os
import pickle
import streamlit as st

# Set page configuration with a heart icon
st.set_page_config(page_title="Heart Disease Prediction",
                   layout="wide",
                   page_icon="❤️")

# Get the absolute path of the directory where 'app.py' is located
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Construct the relative path to your model file from the base directory
model_path = os.path.join(BASE_DIR, 'model', 'heart_disease_model.sav')

# Print the model path to debug
print(f"Model path: {model_path}")

# Load the model
try:
    with open(model_path, 'rb') as model_file:
        heart_disease_model = pickle.load(model_file)
    print("Model loaded successfully.")
except FileNotFoundError as e:
    print(f"Error: {e}")
    
# Getting the working directory of the main.py
##working_dir = os.path.dirname(os.path.abspath(__file__))

# Loading the saved heart disease model
#heart_disease_model = pickle.load(open('model/heart_disease_model.sav', 'rb'))

# Sidebar
st.sidebar.title("Navigation")
selected = st.sidebar.radio(
    "Choose a section:", 
    ["Home", 
     "Heart Disease Prediction", 
     "About Us"]
)

# Home Section
if selected == 'Home':
    st.markdown("<h1 style='text-align: center; color: red;'>Welcome to Heart Disease Prediction App</h1>", unsafe_allow_html=True)
    st.write("""
    This application uses machine learning to predict the likelihood of heart disease in individuals based on their medical information.
    Please navigate to the "Heart Disease Prediction" section to enter your details and get predictions.
    """)

# Heart Disease Prediction Section
if selected == 'Heart Disease Prediction':
    st.markdown("<h1 style='text-align: center; color: red;'>Heart Disease Prediction using Machine Learning</h1>", unsafe_allow_html=True)

    # User input fields
    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age')

    with col2:
        sex = st.selectbox('Sex', options=['Female', 'Male'])

    with col3:
        cp = st.selectbox('Chest Pain Type', options=['Typical Angina', 'Atypical Angina', 
                                                       'Non-Anginal Pain', 'Asymptomatic'])

    with col1:
        trestbps = st.text_input('Resting Blood Pressure (in mm Hg)')

    with col2:
        chol = st.text_input('Serum Cholestoral (in mg/dl)')

    with col3:
        fbs = st.selectbox('Fasting Blood Sugar > 120 mg/dl', options=['False', 'True'])

    with col1:
        restecg = st.selectbox('Resting Electrocardiographic Results', options=['Normal', 'lv hypertrophy', 'st-t abnormality'])

    with col2:
        thalach = st.text_input('Maximum Heart Rate Achieved')

    with col3:
        exang = st.selectbox('Exercise Induced Angina', options=['False', 'True'])

    with col1:
        oldpeak = st.text_input('ST Depression Induced by Exercise')

    with col2:
        slope = st.selectbox('Slope of the Peak Exercise ST Segment', options=['Upsloping', 'Flat', 'Downsloping'])

    with col3:
        ca = st.text_input('Major Vessels Colored by Flourosopy (0-3)')

    with col1:
        thal = st.selectbox('Thalassemia', options=['Normal', 'Fixed Defect', 'Reversible Defect'])

    heart_diagnosis = ''

    # Custom CSS for the button
    st.markdown("""
        <style>
        .custom-button {
            background-color: red !important;
            color: white !important;
            border: none !important;
            padding: 10px 20px;
            font-size: 16px;
            cursor: pointer;
            border-radius: 5px;
        }
        .stButton > button {
            background-color: red !important;
            color: white !important;
            border: none !important;
            padding: 10px 20px;
            font-size: 16px;
            cursor: pointer;
            border-radius: 5px;
        }
        </style>
    """, unsafe_allow_html=True)

    # Creating a button for Prediction
'''    if st.button('Heart Disease Test Result', key='custom_button'):
        user_input = [age, int(sex.split('-')[0].strip()), int(cp.split('-')[0].strip()), 
                      trestbps, chol, int(fbs.split('-')[0].strip()), 
                      int(restecg.split('-')[0].strip()), thalach, int(exang.split('-')[0].strip()), 
                      oldpeak, int(slope.split('-')[0].strip()), ca, int(thal.split('-')[0].strip())]

        user_input = [float(x) if isinstance(x, (int, float)) else x for x in user_input]
        
        heart_prediction = heart_disease_model.predict([user_input])

        if heart_prediction[0] == 1:
            heart_diagnosis = '<span style="color:red; font-size:24px; font-weight:bold;">❤️ The person is at risk of heart disease. ❤️</span>'
        else:
            heart_diagnosis = '<span style="color:green; font-size:24px; font-weight:bold;">💚 The person is not at risk of heart disease. 💚</span>'

    st.markdown(heart_diagnosis, unsafe_allow_html=True)'''
    
    
# Creating a button for Prediction
if st.button('Heart Disease Test Result'):
    user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
    
    # Convert user input to float
    user_input = [float(x) for x in user_input]

    # Make prediction
    heart_prediction = heart_disease_model.predict([user_input])

    # Diagnosis message based on prediction
    if heart_prediction[0] == 1:
        heart_diagnosis = '<span style="color:red; font-size:24px; font-weight:bold;">❤️ The person is at risk of heart disease. ❤️</span>'
    else:
        heart_diagnosis = '<span style="color:green; font-size:24px; font-weight:bold;">💚 The person is not at risk of heart disease. 💚</span>'

    # Display the result
    st.success(heart_diagnosis)



# About Us Section
if selected == 'About Us':
    st.markdown("<h1 style='text-align: center; color: Red;'>About Us</h1>", unsafe_allow_html=True)
    st.write("""
    Welcome to the Heart Disease Prediction App! Our goal is to help individuals assess their risk of heart disease using machine learning algorithms. 
    By providing your medical information, you can receive a prediction that may guide you in seeking medical advice or lifestyle changes.
    
    This project is designed with a user-friendly interface and aims to raise awareness about heart health.
    
    **Contact Us:**  
    If you have any questions or feedback, feel free to reach out!
    """)

# Footer Section
st.markdown("---")
st.write("© 2024 Heart Disease Prediction App. All rights reserved.")
