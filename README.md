#  Heart Disease Prediction Project

## 🔍 Project Overview
This project is a **machine learning application** that predicts the likelihood of **heart disease** based on patient health data.  
It uses the **UCI Heart Disease Dataset**, applies preprocessing, dimensionality reduction (**PCA**), and a trained classification model to provide predictions.  
An interactive **Streamlit web app** allows users to enter their health details and receive **real-time risk assessment** with visualizations.

---

## 📂 Dataset
- **Source:** [UCI Heart Disease Dataset](https://archive.ics.uci.edu/dataset/45/heart+disease)  
- **Features Used:**
  - Age  
  - Sex  
  - Chest pain type  
  - Resting blood pressure  
  - Serum cholesterol  
  - Fasting blood sugar  
  - Resting ECG results  
  - Maximum heart rate achieved  
  - Exercise-induced angina  
  - ST depression  
  - Slope of ST segment  
  - Major vessels colored by fluoroscopy  
  - Thalassemia  

---

## 🛠️ Tools & Libraries
- Python 3.x  
- Pandas  
- NumPy  
- Scikit-learn  
- Matplotlib  
- Streamlit  

---

## 🚀 Steps Performed

### 1️⃣ Define the Problem
Predict whether a patient has **heart disease** based on medical features to support healthcare decision-making.  

### 2️⃣ Load and Explore Data
- Loaded the dataset  
- Performed **exploratory data analysis (EDA)**  
- Handled missing values and categorical features  

### 3️⃣ Preprocessing & Feature Selection
- Applied **OneHotEncoding** and **Scaling** (StandardScaler/MinMaxScaler)  
- Selected relevant features for model training  

### 4️⃣ Dimensionality Reduction
- Applied **Principal Component Analysis (PCA)** to reduce feature space and improve efficiency  

### 5️⃣ Train Classification Model
- Trained a machine learning model  
- Saved the trained pipeline as `models/final_model.pkl`  

### 6️⃣ Evaluate Model
- Assessed performance using:  
  - Accuracy  
  - Precision  
  - Recall  
  - F1-Score  

### 7️⃣ Build Streamlit App
- Developed an interactive UI with **Streamlit**  
- Users input medical details  
- App provides **real-time prediction** with visualization  

---

## 📊 Visualizations
- Correlation heatmap of medical features  
- PCA variance explained plot  
- Classification evaluation metrics  
- Real-time results on Streamlit app  

---

## 📈 Insights
- PCA reduces complexity while maintaining predictive power  
- Patients with higher risk factors (e.g., chest pain, high cholesterol, low heart rate recovery) were more likely classified as **at risk**  
- Model provides a foundation for decision-support tools in healthcare  

---

## 👩‍💻 Author

**Mariam Badr**  
Faculty of Computers & Artificial Intelligence, Cairo University  
[GitHub](https://github.com/Mariam-Badr-MB) – [LinkedIn](https://www.linkedin.com/)  

---

## 🤝 Contributing
This project is **open for contributions ❤️**    
Feel free to:  
- Suggest improvements  
- Add new visualizations or evaluation metrics  
- Extend the analysis with other models (Logistic Regression, Random Forest, XGBoost, etc.)  
- Deploy on cloud platforms  

Your contributions are **welcome** and highly appreciated to make this project even more useful for healthcare and prediction research.  
