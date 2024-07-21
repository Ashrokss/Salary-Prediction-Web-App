import streamlit as st
from joblib import load
import pandas as pd

# Load the trained model
model_path = 'trained_model.joblib'
loaded_model = load(model_path)

# Title of the app
st.title('Salary Prediction App')

# Input fields for user
education_level = st.selectbox('Education Level', ['Bachelor', 'Master', 'PhD'])
experience = st.number_input('Years of Experience')
gender = st.selectbox('Gender', ['Female', 'Male'])

# Convert gender to dummy variables
gender_female = 1 if gender == 'Female' else 0
gender_male = 1 if gender == 'Male' else 0

# Map education level to numerical values
education_mapping = {'Bachelor': 0, 'Master': 1, 'PhD': 2}
education_level_encoded = education_mapping[education_level]

# Prepare the input data for prediction
input_data = pd.DataFrame({
    'Education Level': [education_level_encoded],
    'Years of Experience': [experience],
    'Gender_Female': [gender_female],
    'Gender_Male': [gender_male]
})

# Ensure the input data columns match the model's training columns and order
required_columns = ['Education Level', 'Years of Experience', 'Gender_Female', 'Gender_Male']
input_data = input_data[required_columns]

# Make prediction
if st.button('Predict Salary'):
    prediction = loaded_model.predict(input_data)
    salary_in_dollars = prediction[0]  # Output in dollars
    st.write(f'Predicted Salary: ${salary_in_dollars:,.2f} USD')
