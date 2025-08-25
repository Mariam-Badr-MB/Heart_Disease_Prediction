import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load('models/final_pipeline_model.pkl')

# App Title
st.title("❤️ Heart Disease Risk Prediction")
st.write("This application predicts the risk of **heart disease** based on user input features.")

st.sidebar.header('🧪 Patient Test Results Input')
st.sidebar.markdown("Please provide the following information to predict your heart disease risk.")

# ---------------------------
# Function to get user input
# ---------------------------
def user_input_features():
    age = st.sidebar.slider("Age (years)", 20, 100, 50)

    sex = st.sidebar.radio("Sex", ["Male", "Female"])
    sex = 1 if sex == "Male" else 0

    cp = st.sidebar.selectbox("Chest Pain Type", [
        "Typical Angina",
        "Atypical Angina",
        "Non-anginal Pain",
        "Asymptomatic"
    ])
    cp = ["Typical Angina", "Atypical Angina", "Non-anginal Pain", "Asymptomatic"].index(cp)

    trestbps = st.sidebar.slider("Resting Blood Pressure (mm Hg)", 80, 200, 120)

    chol = st.sidebar.slider("Serum Cholesterol (mg/dl)", 100, 600, 200)

    fbs = st.sidebar.radio("Fasting Blood Sugar (>120 mg/dl)", ["No", "Yes"])
    fbs = 1 if fbs == "Yes" else 0

    restecg = st.sidebar.selectbox("Resting ECG Results", [
        "Normal",
        "ST-T wave abnormality",
        "Left ventricular hypertrophy"
    ])
    restecg = ["Normal", "ST-T wave abnormality", "Left ventricular hypertrophy"].index(restecg)

    thalach = st.sidebar.slider("Maximum Heart Rate Achieved (bpm)", 60, 220, 150)

    exang = st.sidebar.radio("Exercise Induced Angina", ["No", "Yes"])
    exang = 1 if exang == "Yes" else 0

    oldpeak = st.sidebar.slider("ST Depression (Oldpeak)", 0.0, 6.0, 1.0, step=0.1)

    slope = st.sidebar.selectbox("Slope of Peak Exercise ST Segment", [
        "Upsloping",
        "Flat",
        "Downsloping"
    ])
    slope = ["Upsloping", "Flat", "Downsloping"].index(slope)

    ca = st.sidebar.selectbox("Number of Major Vessels (0-3)", [0, 1, 2, 3])

    thal = st.sidebar.selectbox("Thalassemia", [
        "Normal",
        "Fixed Defect",
        "Reversible Defect"
    ])
    thal = ["Normal", "Fixed Defect", "Reversible Defect"].index(thal)

    # Collect features in DataFrame
    input_data = pd.DataFrame({
        'age': [age],
        'sex': [sex],
        'cp': [cp],
        'trestbps': [trestbps],
        'chol': [chol],
        'fbs': [fbs],
        'restecg': [restecg],
        'thalach': [thalach],
        'exang': [exang],
        'oldpeak': [oldpeak],
        'slope': [slope],
        'ca': [ca],
        'thal': [thal]
    })

    return input_data

# ---------------------------
# Get input & display
# ---------------------------
input_df = user_input_features()

st.subheader('📝 Input Data')
st.write(input_df)

# ---------------------------
# Prediction
# ---------------------------
if st.button('🔮 Predict'):
    prediction = model.predict(input_df)[0]
    prediction_proba = model.predict_proba(input_df)[0]

    risk = 'High Risk ⚠️' if prediction == 1 else 'Low Risk ✅'

    st.subheader('📊 Prediction')
    st.write(f'Heart Disease Risk: **{risk}**')

    st.subheader('📈 Prediction Probability')
    st.write(f'Probability of Low Risk (0): **{prediction_proba[0]:.2f}**')
    st.write(f'Probability of High Risk (1): **{prediction_proba[1]:.2f}**')
    
