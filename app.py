import streamlit as st
import pickle
import pandas as pd

# Load trained model
with open("loan_prediction_model.pkl", "rb") as file:
    model = pickle.load(file)

# App title
st.title("🏦 Loan Approval Prediction")

st.write("Enter applicant details to check **Loan Approval Status**.")

# ---- Input fields ----
gender = st.selectbox("Gender", ["Male", "Female"])
married = st.selectbox("Married", ["Yes", "No"])
dependents = st.selectbox("Dependents", ["0", "1", "2", "3+"])
education = st.selectbox("Education", ["Graduate", "Not Graduate"])
self_employed = st.selectbox("Self Employed", ["Yes", "No"])
property_area = st.selectbox("Property Area", ["Urban", "Semiurban", "Rural"])

applicant_income = st.number_input("Applicant Income", min_value=0)
coapplicant_income = st.number_input("Coapplicant Income", min_value=0)
loan_amount = st.number_input("Loan Amount", min_value=0)
loan_term = st.number_input("Loan Amount Term (months)", value=360)
credit_history = st.selectbox("Credit History", [1.0, 0.0])

# ---- Predict button ----
if st.button("Predict Loan Status"):
    input_data = pd.DataFrame([{
        "Gender": gender,
        "Married": married,
        "Dependents": dependents,
        "Education": education,
        "Self_Employed": self_employed,
        "ApplicantIncome": applicant_income,
        "CoapplicantIncome": coapplicant_income,
        "LoanAmount": loan_amount,
        "Loan_Amount_Term": loan_term,
        "Credit_History": credit_history,
        "Property_Area": property_area
    }])

    prediction = model.predict(input_data)[0]

    if prediction == "Y":
        st.success("✅ Loan Approved")
    else:
        st.error("❌ Loan Rejected")
