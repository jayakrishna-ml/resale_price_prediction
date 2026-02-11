import streamlit as st
import requests
import joblib

st.set_page_config(
    page_title="SINGAPOOR Resale Flat Price Predictor",
    page_icon="🏠",
    layout="centered"
)

API_URL = "https://resale-price-prediction-9hbf.onrender.com/predict"

st.markdown("## 🏠 Singapore Resale Flat Price Prediction")
st.write("Predict resale price using the trained ML model")

import os

BASE_DIR = os.path.dirname(__file__)
uniques_path = os.path.join(BASE_DIR, "unique_values.pkl")

uniques = joblib.load(uniques_path)

st.subheader("Flat Details")

col1,col2=st.columns(2)

with col1:
    town=st.selectbox("Town",uniques["town"])

    street_name=st.selectbox("Street Name",uniques["street_name"])

    year=st.selectbox(
        "Transaction Year",
        list(range(1990,2031)),
        index=22
    )

    month_names={
        1:"January",2:"February",3:"March",4:"April",5:"May",6:"June",
        7:"July",8:"August",9:"September",10:"October",11:"November",12:"December"
    }
    month=st.selectbox(
        "Transaction Month",
        options=list(month_names.keys()),
        format_func=lambda x:month_names[x]
    )

with col2:
    floor_area_sqm=st.slider("Floor Area (sqm)",20,200,70)
    remaining_lease=st.slider("Remaining Lease (years)",1,99,65)
    flat_type=st.selectbox("Flat Type",uniques["flat_type"])
    flat_model=st.selectbox("Flat Model",uniques["flat_model"])
    storey_range=st.selectbox("Storey Range",uniques["storey_range"])

st.divider()

predict =st.button("Predict Flat Resale Price", use_container_width=True)

if predict:

    payload={
        "year":year,
        "month":month,
        "town":town,
        "street_name":street_name,
        "flat_type":flat_type,
        "flat_model":flat_model,
        "storey_range":storey_range,
        "floor_area_sqm":floor_area_sqm,
        "remaining_lease":remaining_lease
    }

    try:
        response=requests.post(API_URL,json=payload)

        try:
            data=response.json()
        except ValueError:
            st.error("Backend did not return valid JSON")
            st.stop()

        if response.status_code==200:
            if "prediction_price" in data:
                price=data["prediction_price"]
                st.success(f"Estimate Resale Flat Price: SGD {price:,.0f}")
            else:
                st.error(f"Unexpected JSON format: {data}")
        else:
            st.error(f"API Error {response.status_code}: {data}")
    
    except requests.exceptions.ConnectionError:
        st.error("cannot connect to FastAPI backend.")
    except requests.exceptions.Timeout:
        st.error("API request timed out.")
    except Exception as e:
        st.error(f"Unexpected errorr: {e}")

    st.caption("This is a model-based estimate, not an official valuation.")

st.divider()
st.caption("Built with Machine Learning - Deployed using Streamlit")
    
