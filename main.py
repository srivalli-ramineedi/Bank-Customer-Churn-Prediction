'''import streamlit as st
import requests
import json

st.title("🏦 Bank Customer Churn Prediction System")
st.write("Enter customer details to predict churn probability")

# Input form
credit_score = st.number_input("Credit Score", 300, 900, 600)
country = st.selectbox("Country", ["France", "Germany", "Spain"])
gender = st.selectbox("Gender", ["Male", "Female"])
age = st.number_input("Age", 18, 100, 40)
tenure = st.number_input("Tenure (Years)", 0, 10, 5)
balance = st.number_input("Balance", 0.0, 250000.0, 50000.0)
products_number = st.number_input("Products Number", 1, 4, 2)
credit_card = st.selectbox("Credit Card (1=Yes, 0=No)", [0, 1])
active_member = st.selectbox("Active Member (1=Yes, 0=No)", [0, 1])
estimated_salary = st.number_input("Estimated Salary", 0.0, 200000.0, 70000.0)

# Button
if st.button("Predict Churn"):

    url = "http://127.0.0.1:8000/evaluate-churn"

    payload = {
        "credit_score": credit_score,
        "country": country,
        "gender": gender,
        "age": age,
        "tenure": tenure,
        "balance": balance,
        "products_number": products_number,
        "credit_card": credit_card,
        "active_member": active_member,
        "estimated_salary": estimated_salary
    }

    response = requests.post(url, json=payload)

    result = response.json()

    st.subheader("Prediction Result")

    if result["prediction"] == 1:
        st.error("⚠ High Risk: Customer will leave the bank")
    else:
        st.success("✅ Low Risk: Customer will stay")

    st.write("Churn Probability:", result["churn_probability"], "%")'''

import streamlit as st
import requests

st.set_page_config(
    page_title="Bank Customer Churn Prediction",
    page_icon="🏦",
    layout="centered"
)

st.title("🏦 Bank Customer Churn Prediction System")
st.write("Enter customer details to predict churn probability")

# Inputs
credit_score = st.number_input("Credit Score", min_value=300, max_value=900, value=600)

country = st.selectbox(
    "Country",
    ["France", "Germany", "Spain"]
)

gender = st.selectbox(
    "Gender",
    ["Male", "Female"]
)

age = st.number_input(
    "Age",
    min_value=18,
    max_value=100,
    value=40
)

tenure = st.number_input(
    "Tenure (Years)",
    min_value=0,
    max_value=10,
    value=5
)

balance = st.number_input(
    "Balance",
    min_value=0.0,
    value=50000.0
)

products_number = st.number_input(
    "Products Number",
    min_value=1,
    max_value=4,
    value=2
)

credit_card = st.selectbox(
    "Credit Card",
    [0, 1],
    format_func=lambda x: "Yes" if x == 1 else "No"
)

active_member = st.selectbox(
    "Active Member",
    [0, 1],
    format_func=lambda x: "Yes" if x == 1 else "No"
)

estimated_salary = st.number_input(
    "Estimated Salary",
    min_value=0.0,
    value=70000.0
)

# Predict Button
if st.button("Predict Churn"):

    api_url = "https://bank-customer-churn-prediction-10bz.onrender.com/evaluate-churn"

    payload = {
        "credit_score": credit_score,
        "country": country,
        "gender": gender,
        "age": age,
        "tenure": tenure,
        "balance": balance,
        "products_number": products_number,
        "credit_card": credit_card,
        "active_member": active_member,
        "estimated_salary": estimated_salary
    }

    try:
        response = requests.post(
            api_url,
            json=payload,
            timeout=30
        )

        response.raise_for_status()

        result = response.json()

        st.subheader("Prediction Result")

        prediction = result.get("prediction")
        probability = result.get("churn_probability")

        if prediction == 1:
            st.error("⚠ High Risk: Customer is likely to leave the bank")
        else:
            st.success("✅ Low Risk: Customer is likely to stay")

        st.metric(
            "Churn Probability",
            f"{probability:.2f}%"
        )

        st.json(result)

    except requests.exceptions.RequestException as e:
        st.error(f"API Connection Error: {e}")

    except Exception as e:
        st.error(f"Unexpected Error: {e}")
