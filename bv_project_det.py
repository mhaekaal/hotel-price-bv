import streamlit as st 
from datetime import datetime
import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.preprocessing import StandardScaler
import streamlit.components.v1 as components
import plotly.express as px
import pickle



def bv_project_det():
    st.markdown(
        '''
            <h1 style='text-align: center; font-size:25px;'>
               Predicting Hotel Rental Price per Night
            </h1>
        ''',
        unsafe_allow_html=True
    )
    st.markdown(
        '''
        ''',
    )
    st.subheader("Introduction")
    st.write("""
        This project aims to develop a machine learning model that predicts hotel rental prices per night
        based on various factors such as location, amenities, demand trends, 
        seasonality, and customer reviews. 
        """)
    st.subheader("Goal")
    st.write("""
        To build a predictive model that accurately estimates hotel rental prices per night, enabling data-driven pricing decisions that enhance hotel profitability and market competitiveness.
    """)

    st.subheader("Try to Predict!")

    col1, col2, col3 = st.columns(3)

    with col1:
        bedrooms = st.number_input("Enter Number of Bedrooms:", min_value=1, max_value=10, value=1)
        bathrooms = st.number_input("Enter Number of Bathrooms:", min_value=1, max_value=10, value=1)

        agency = st.selectbox("Choose Agency:", ["Konang", "Agus Weda", "Bukit Vista"])
        agency_dict = {"Konang": 0, "Agus Weda": 1, "Bukit Vista": 2}
        agency = agency_dict[agency]

        city = st.selectbox("Choose City:", ["Bali", "Nusa Penida", "Yogyakarta"])
        city_dict = {"Bali": 0, "Nusa Penida": 1, "Yogyakarta": 2}
        city = city_dict[city]

        area = st.selectbox("Choose Area:", 
                            ["Canggu", "Nusa Penida", "Bingin", "Uluwatu", "Ungasan", "Yogyakarta", "Ubud", "Jimbaran", "Nusa Dua", "Pecatu", 
                             "Badung, Ungasan", "Badung", "Balangan", "Umalas"])
        area_dict = {area: i for i, area in enumerate(
            ["Canggu", "Nusa Penida", "Bingin", "Uluwatu", "Ungasan", "Yogyakarta", "Ubud", "Jimbaran", "Nusa Dua", "Pecatu", 
             "Badung, Ungasan", "Badung", "Balangan", "Umalas"])}
        area = area_dict[area]

        number_of_guests = st.number_input("Enter Number of Guests:", min_value=1, max_value=10, value=1)

    with col2:
        amazing_pool = st.toggle("Amazing Pool", value=False)
        pool_view = st.toggle("Pool View", value=False)
        surfing = st.toggle("Surfing", value=False)
        jungle_view = st.toggle("Jungle View", value=False)
        islandlife = st.toggle("Island Life", value=False)
        guest_house = st.toggle("Guest House", value=False)

    with col3:
        rice_paddy_view = st.toggle("Rice Paddy View", value=False)
        tropical = st.toggle("Tropical", value=False)
        ocean_view = st.toggle("Ocean View", value=False)
        beachfront = st.toggle("Beach Front", value=False)
        golfing = st.toggle("Golfing", value=False)
        amazing_view = st.toggle("Amazing View", value=False)

    if st.button("Predict"):
        data = [bedrooms, bathrooms, agency, city, area, number_of_guests,
                amazing_pool, pool_view, surfing, jungle_view, islandlife, guest_house,
                rice_paddy_view, tropical, ocean_view, beachfront, golfing, amazing_view]

        # Load scaler and model
        try:
            with open("scaler-detail.pkl", "rb") as f:
                scaler = pickle.load(f)
            with open("modelDT-detail.pkl", "rb") as f:
                model = pickle.load(f)

            columns = ['bedrooms', 'bathrooms', 'agency', 'city', 'area', 'number_of_guests',
                       'Amazing pool', 'Pool view', 'Surfing', 'Jungle View', 'Island life', 'Guest House',
                       'Rice paddy view', 'Tropical', 'Ocean view', 'Beachfront', 'Golfing', 'Amazing View']

            input_data_df = pd.DataFrame([data], columns=columns)
            std_data = scaler.transform(input_data_df)
            prediction = model.predict(std_data)

            st.success(f"Predicted Hotel Rental: ${prediction[0]:.2f}")

        except FileNotFoundError:
            st.error("Model or scaler file not found. Please upload `model.pkl` and `scaler.pkl`.")
        except Exception as e:
            st.error(f"An error occurred: {e}")




  
