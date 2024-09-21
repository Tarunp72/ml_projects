import streamlit as st
import pandas as pd
import joblib  # to load the saved model

# Load the trained model (adjust the path as needed)
model = joblib.load('random_forest_model.pkl')

# Streamlit App Title
st.title("Company Profit Prediction App")

# Input section
st.header("Enter the company's investments manually:")

# User input fields for R&D Spend, Administration, and Marketing Spend using text input
rd_spend = st.text_input("Enter R&D Spend (in dollars)", "0")
administration = st.text_input("Enter Administration (in dollars)", "0")
marketing_spend = st.text_input("Enter Marketing Spend (in dollars)", "0")

# State dropdown with user-friendly labels
state = st.selectbox(
    "Select the state", 
    options=[0, 1, 2], 
    format_func=lambda x: {0: "Florida", 1: "California", 2: "New York"}.get(x)
)

# Predict button
if st.button("Predict Profit"):
    try:
        # Convert text inputs to float
        rd_spend = float(rd_spend)
        administration = float(administration)
        marketing_spend = float(marketing_spend)

        # Prepare the input data in the required format
        input_data = pd.DataFrame({
            'R&D Spend': [rd_spend],
            'Administration': [administration],
            'Marketing Spend': [marketing_spend],
            'State_Enc': [state]  # Encoded state value
        })

        # Make the prediction using the loaded model
        predicted_profit = model.predict(input_data)
        
        # Display the prediction result
        st.subheader(f"Predicted Profit: ${predicted_profit[0]:,.2f}")

    except ValueError:
        st.error("Please enter valid numerical values for investments.")
