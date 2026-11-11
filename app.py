
import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("models/spam_model.pkl")

# Page configuration
st.set_page_config(
    page_title="Email Spam Detector",
    page_icon="📧",
    layout="centered"
)

# Title
st.title("📧 Email Spam Detection System")

st.write(
    "Enter the numerical email features below "
    "to predict whether an email is Spam or Not Spam."
)

# Load dataset columns
df = pd.read_csv("dataset/cleaned_spambase.csv")
feature_columns = df.drop("Class", axis=1).columns

# Input fields
st.subheader("Email Features")

input_values = {}

for feature in feature_columns:
    input_values[feature] = st.number_input(
        feature,
        min_value=0.0,
        value=0.0,
        step=0.01,
        format="%.2f"
    )

# Prediction button
if st.button("Predict Email", use_container_width=True):

    input_df = pd.DataFrame(
        [input_values],
        columns=feature_columns
    )

    prediction = model.predict(input_df)[0]

    probability = model.predict_proba(input_df)[0]

    if prediction == 1:
        st.error("🚨 This email is SPAM!")
    else:
        st.success("✅ This email is NOT SPAM!")

    st.write(
        f"Spam probability: {probability[1] * 100:.2f}%"
    )

    st.write(
        f"Not Spam probability: {probability[0] * 100:.2f}%"
    )
