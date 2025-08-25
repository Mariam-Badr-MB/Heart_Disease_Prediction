import streamlit as st
import pandas as pd
import joblib

model = joblib.load('models/final_pipeline_model.pkl')

st.title("Heart Disease Risk Prediction")
st.write("This application predicts the risk of **heart disease** based on user input features.")

st.sidebar.header('User Input Features')
st.sidebar.markdown("""
Please provide the following information to predict your heart disease risk.
""")

# User input features
# Using sidebar for input to enhance UI

def user_input_features():

    age = st.sidebar.slider("Age", 1, 120, 50)
    sex = st.sidebar.selectbox("Sex", [0, 1], format_func=lambda x: "Male" if x == 1 else "Female")
    cp = st.sidebar.selectbox("Chest Pain Type (cp)", [0, 1, 2, 3])
    trestbps = st.sidebar.slider("Resting Blood Pressure (mm Hg)", 80, 200, 120)
    chol = st.sidebar.slider("Serum Cholesterol (mg/dl)", 100, 600, 200)
    fbs = st.sidebar.selectbox("Fasting Blood Sugar > 120 mg/dl", [0, 1])
    restecg = st.sidebar.selectbox("Resting ECG Results", [0, 1, 2])
    thalach = st.sidebar.slider("Maximum Heart Rate Achieved", 60, 220, 150)
    exang = st.sidebar.selectbox("Exercise Induced Angina", [0, 1])
    oldpeak = st.sidebar.slider("ST Depression (Oldpeak)", 0.0, 6.0, 1.0, step=0.1)
    slope = st.sidebar.selectbox("Slope of Peak Exercise ST Segment", [0, 1, 2])
    ca = st.sidebar.selectbox("Number of Major Vessels (0-3)", [0, 1, 2, 3])
    thal = st.sidebar.selectbox("Thalassemia", [3, 6, 7])

    # Collect features in DataFrame
    input_data = pd.DataFrame({
        'age': age,
        'sex': sex,
        'cp': cp,
        'trestbps': trestbps,
        'chol': chol,
        'fbs': fbs,
        'restecg': restecg,
        'thalach': thalach,
        'exang': exang,
        'oldpeak': oldpeak,
        'slope': slope,
        'ca': ca,
        'thal': thal

    }, index=[0])

    return input_data

# Get user input features
input_df = user_input_features()

st.subheader('Input Data')
st.write(input_df)


if st.button('Predict'):

    prediction = model.predict(input_df)[0]
    prediction_proba = model.predict_proba(input_df)[0]

    risk = 'High Risk' if prediction == 1 else 'Low Risk'

    st.subheader('Prediction')
    st.write(f'Heart Disease Risk: **{risk}**')

    st.subheader('Prediction Probability')
    st.write(f'Probability of Low Risk (0): **{prediction_proba[0]:.2f}**')
    st.write(f'Probability of High Risk (1): **{prediction_proba[1]:.2f}**')

