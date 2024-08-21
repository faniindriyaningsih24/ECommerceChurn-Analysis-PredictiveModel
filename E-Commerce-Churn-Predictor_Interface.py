import streamlit as st
import pandas as pd
import pickle

# Load the model
with open("ModelXGBTuned_beta.sav", "rb") as model_file:
    final_model = pickle.load(model_file)

st.title('E-Commerce Customer Churn Predictor Machine')

# ========= INPUTS =========

# SELECTBOX for categorical features
preferred_login_device = st.selectbox('Preferred Login Device', ['Mobile Phone', 'Computer'])
city_tier = st.selectbox('City Tier', [1, 2, 3])
preferred_payment_mode = st.selectbox('Preferred Payment Mode', ['Debit Card', 'UPI', 'Credit Card', 'Cash on Delivery', 'E-wallet'])
gender = st.selectbox('Gender', ['Female', 'Male'])
prefered_order_cat = st.selectbox('Preferred Order Category', ['Laptop & Accessory', 'Mobile Phone', 'Others', 'Fashion', 'Grocery'])
marital_status = st.selectbox('Marital Status', ['Single', 'Divorced', 'Married'])

# NUMBERINPUT for numerical features
tenure = st.number_input('Tenure (months)', min_value=0.0, step=1.0)
warehouse_to_home = st.number_input('Warehouse to Home (km)', min_value=0.0, step=1.0)
number_of_device_registered = st.number_input('Number of Devices Registered', min_value=1, step=1)
satisfaction_score = st.number_input('Satisfaction Score', min_value=1, max_value=5, step=1)
number_of_address = st.number_input('Number of Addresses', min_value=1, step=1)
complain = st.selectbox('Complain', [0, 1])
order_amount_hike_from_last_year = st.number_input('Order Amount Hike from Last Year (%)', min_value=0.0, step=1.0)
day_since_last_order = st.number_input('Days Since Last Order', min_value=0.0, step=1.0)
cashback_amount = st.number_input('Cashback Amount', min_value=0.0, step=1.0)

# Prepare input data
input_data = {
    "Tenure": tenure,
    "PreferredLoginDevice": preferred_login_device,
    "CityTier": city_tier,
    "WarehouseToHome": warehouse_to_home,
    "PreferredPaymentMode": preferred_payment_mode,
    "Gender": gender,
    "NumberOfDeviceRegistered": number_of_device_registered,
    "PreferedOrderCat": prefered_order_cat,
    "SatisfactionScore": satisfaction_score,
    "MaritalStatus": marital_status,
    "NumberOfAddress": number_of_address,
    "Complain": complain,
    "OrderAmountHikeFromlastYear": order_amount_hike_from_last_year,
    "DaySinceLastOrder": day_since_last_order,
    "CashbackAmount": cashback_amount
}

# Convert input data to DataFrame
input_df = pd.DataFrame([input_data])

# Prediction
if st.button('Predict Churn'):
    prediction = final_model.predict(input_df)
    prediction_proba = final_model.predict_proba(input_df)
    
    if prediction[0] == 1:
        st.write("Customers are likely to **CHURN**.")
    else:
        st.write("Customers are **NOT to CHURN**.")
    
    st.write(f"Probability of **Churn**: {prediction_proba[0][1]*100:.2f}%")
