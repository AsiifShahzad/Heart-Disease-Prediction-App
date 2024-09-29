import os
import pickle
import streamlit as st

# Set page configuration with a heart icon
st.set_page_config(page_title="Heart Disease Prediction", layout="wide", page_icon="❤️")

# Get the absolute path of the directory where 'app.py' is located
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(BASE_DIR, 'model', 'heart_disease_model.sav')

# Load the model with caching
@st.cache_resource
def load_model():
    try:
        with open(model_path, 'rb') as model_file:
            return pickle.load(model_file)
    except FileNotFoundError as e:
        st.error(f"Model file not found: {e}")
        return None

heart_disease_model = load_model()

# Check if the model loaded successfully
if heart_disease_model is None:
    st.error("Failed to load the heart disease model. Please check the model file.")

# Sidebar Navigation
st.sidebar.title("Navigation")
selected = st.sidebar.radio("Choose a section:", ["Home", "Heart Disease Prediction", "About Us"])

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
        age = st.number_input('Age', min_value=0)  # Use number_input for numeric input

    with col2:
        sex = st.selectbox('Sex', options=['Female', 'Male'])

    with col3:
        cp = st.selectbox('Chest Pain Type', options=['Typical Angina', 'Atypical Angina', 
                                                       'Non-Anginal Pain', 'Asymptomatic'])

    with col1:
        trestbps = st.number_input('Resting Blood Pressure (in mm Hg)', min_value=0)  # Use number_input

    with col2:
        chol = st.number_input('Serum Cholestoral (in mg/dl)', min_value=0)  # Use number_input

    with col3:
        fbs = st.selectbox('Fasting Blood Sugar > 120 mg/dl', options=['False', 'True'])

    with col1:
        restecg = st.selectbox('Resting Electrocardiographic Results', options=['Normal', 'lv hypertrophy', 'st-t abnormality'])

    with col2:
        thalach = st.number_input('Maximum Heart Rate Achieved', min_value=0)  # Use number_input

    with col3:
        exang = st.selectbox('Exercise Induced Angina', options=['False', 'True'])

    with col1:
        oldpeak = st.number_input('ST Depression Induced by Exercise', min_value=0.0)  # Use number_input

    with col2:
        slope = st.selectbox('Slope of the Peak Exercise ST Segment', options=['Upsloping', 'Flat', 'Downsloping'])

    with col3:
        ca = st.number_input('Major Vessels Colored by Flourosopy (0-3)', min_value=0)  # Use number_input

    with col1:
        thal = st.selectbox('Thalassemia', options=['Normal', 'Fixed Defect', 'Reversible Defect'])

    # Button for Prediction
    if st.button('Heart Disease Test Result'):
        user_input = [
            float(age),
            1 if sex == 'Male' else 0,  # Convert sex to binary
            cp.index(cp),  # Convert cp to numeric
            float(trestbps),
            float(chol),
            1 if fbs == 'True' else 0,  # Convert fbs to binary
            restecg.index(restecg),  # Convert restecg to numeric
            float(thalach),
            1 if exang == 'True' else 0,  # Convert exang to binary
            float(oldpeak),
            slope.index(slope),  # Convert slope to numeric
            float(ca),
            thal.index(thal)  # Convert thal to numeric
        ]

        # Make prediction
        heart_prediction = heart_disease_model.predict([user_input])

        # Diagnosis message based on prediction
        if heart_prediction[0] == 1:
            heart_diagnosis = '<span style="color:red; font-size:24px; font-weight:bold;">❤️ The person is at risk of heart disease. ❤️</span>'
        else:
            heart_diagnosis = '<span style="color:green; font-size:24px; font-weight:bold;">💚 The person is not at risk of heart disease. 💚</span>'

        # Display the result
        st.markdown(heart_diagnosis, unsafe_allow_html=True)

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
