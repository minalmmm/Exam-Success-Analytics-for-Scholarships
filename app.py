import streamlit as st
import pandas as pd
import numpy as np
import joblib
st.image('C:\data science material\my project\project_11\img11.jpg', use_column_width=True)
# Load the trained model
model = joblib.load('gradient_boosting_model.pkl')

# Streamlit app header
st.title('Scholarship Prediction App')
st.write('Enter the student details to predict scholarship success.')

# Create input fields for features
math_score = st.number_input('Math Score', step=0.1)
science_score = st.number_input('Science Score', step=0.1)
english_score = st.number_input('English Score', step=0.1)
hours_studied = st.number_input('Hours Studied', step=0.1)
extracurriculars = st.selectbox('Extracurricular Activities', [0, 1], format_func=lambda x: "No" if x == 0 else "Yes")

# Create engineered features (interaction terms, ratios, etc.)
math_science_interaction = math_score * science_score
math_english_interaction = math_score * english_score
hours_to_math = hours_studied / (math_score + 1e-5)
hours_to_science = hours_studied / (science_score + 1e-5)

# Bin the 'Hours_Studied' for categorization
study_hours_bin = pd.cut([hours_studied],
                         bins=[-np.inf, -1, 0, 1, np.inf],
                         labels=['Very Low', 'Low', 'Medium', 'High'],
                         right=False)[0]

activity_study_bin = extracurriculars * hours_studied

# Prepare the input data for prediction
input_data = pd.DataFrame({
    'Math_Score': [math_score],
    'Science_Score': [science_score],
    'English_Score': [english_score],
    'Hours_Studied': [hours_studied],
    'Extracurriculars': [extracurriculars],
    'Math_Science_Interaction': [math_science_interaction],
    'Math_English_Interaction': [math_english_interaction],
    'Hours_to_Math': [hours_to_math],
    'Hours_to_Science': [hours_to_science],
    'Study_Hours_Bin': [study_hours_bin],
    'Activity_Study_Bin': [activity_study_bin]
})

# One-hot encode the 'Study_Hours_Bin' column
input_data = pd.get_dummies(input_data, columns=['Study_Hours_Bin'], drop_first=True)

# Ensure all columns match the trained model (add missing columns with 0 if needed)
expected_cols = model.feature_names_in_.tolist()

# Check for missing columns and add them with 0 if necessary
for col in expected_cols:
    if col not in input_data.columns:
        input_data[col] = 0  # Add missing columns with 0
input_data = input_data[expected_cols]  # Reorder columns to match the model

# When the user submits the form, perform prediction
if st.button('Predict Scholarship'):
    prediction = model.predict(input_data)
    if prediction[0] == 1:
        st.success('This student is likely to win a scholarship!')
    else:
        st.error('This student is not likely to win a scholarship.')
