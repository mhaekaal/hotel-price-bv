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
            <figure style='text-align:center;'>
                <img src='https://img.freepik.com/free-vector/hotel-building-tropical-country-with-palms-cartoon-icon_1284-63176.jpg?t=st=1740556535~exp=1740560135~hmac=f8be5e83778348e7d96fbc4a123ad40fe96354634b4a763b1127833f8178331c&w=900'>
            </figure>
        ''',
        unsafe_allow_html=True
    )
    st.markdown(
        '''
            <h1 style='text-align: left; font-size:20px;'>
               Introduction
            </h1>
        ''',
        unsafe_allow_html=True
    )
    st.markdown(
        '''<h1 style='text-align:left;font-size:15px;font-weight:normal;text-indent:30px; line-height:2;'>
        This project aims to develop a machine learning model that predicts hotel rental prices per night
        based on various factors such as location, amenities, demand trends, 
        seasonality, and customer reviews. By leveraging historical booking data and external influencing factors, 
        the model provides accurate price estimations to help hotel managers optimize pricing strategies and improve revenue management.
        </h1>
        ''', unsafe_allow_html=True
    )
    st.markdown(
        '''
            <h1 style='text-align: left; font-size:20px;'>
               Goal
            </h1>
        ''',
        unsafe_allow_html=True
    )
    st.markdown(
        'To build a predictive model that accurately estimates hotel rental prices per night, enabling data-driven pricing decisions that enhance hotel profitability and market competitiveness.'
    )

    st.markdown(
        '''
            <h1 style='text-align: left; font-size:20px;'>
               Try to Prediction!
            </h1>
        ''',
        unsafe_allow_html=True
    )

#__________________________________Predict__________________
    # CSS box


    col1, col2, col3 = st.columns(3)

    with col1:
    # Get Bedrooms
        bedrooms = st.number_input('Enter Number of Bedrooms:',
        min_value= 1,
        max_value= 10,
        value=1,
        placeholder='Please Insert Number'
        )
        
    # Get Bathrooms
        bathrooms = st.number_input('Enter Number of Bathrooms:',
        min_value= 1,
        max_value= 10,
        value=1,
        placeholder='Please Insert Number'
        )
        
    # Get Agency
        agency = st.selectbox(
        'Choose Agency:',
        ['Konang', 'Agus Weda', 'Bukit Vista'],
    )
        if agency == 'Konang':
            agency = 0
        elif agency == 'Agus Weda':
            agency = 1
        elif agency == 'Bukit Vista':
            agency = 2
        elif agency == 'Please Select':
            agency = None
    # Get City
        city = st.selectbox(
        'Choose City:',
        ['Bali', 'Nusa Penida', 'Yogyakarta'],
    )
        if city == 'Bali':
            city = 0
        elif city == 'Nusa Penida':
            city = 1
        elif city == 'Yogyakarta':
            city = 2
        elif city == 'Please Select City':
            city = None
 # Get area
        area = st.selectbox(
        'Choose Area:',
        ['Canggu', 'Nusa Penida', 'Bingin', 'Uluwatu', 'Ungasan', 'Yogyakarta', 'Ubud', 'Jimbaran', 'Nusa Dua', 'Pecatu', 'Badung, Ungasan', 'Badung', 'Balangan', 'Umalas'],
    )
        if area == 'Canggu':
            area = 0
        elif area == 'Nusa Penida':
            area = 1
        elif area == 'Bingin':
            area = 2
        elif area == 'Uluwatu':
            area = 3
        elif area == 'Ungasan':
            area = 4
        elif area == 'Yogyakarta':
            area = 5
        elif area == 'Ubud':
            area = 6
        elif area == 'Jimbaran':
            area = 7
        elif area == 'Nusa Dua':
            area = 8
        elif area == 'Pecatu':
            area = 9
        elif area == 'Badung, Ungasan':
            area = 10
        elif area == 'Badung':
            area = 11
        elif area == 'Balangan':
            area = 12
        elif area == 'Umalas':
            area = 13
        elif area == 'Please Select Area':
            area = None
          
    #Get number_of_guests
        number_of_guests = st.number_input('Enter number of guest:',
        min_value= 1,
        max_value= 10,
        value= 1,
        placeholder='Please Insert Number'
        )
      
    with col2:
    # feature amazing pool
        amazing_pool_yes = 1
        amazing_pool = st.toggle("Amazing Pool",
                                 value=bool(amazing_pool_yes)
        )
    # feature Pool View
        poolview_yes = 1
        pool_view = st.toggle("Pool View",
                                 value=bool(poolview_yes)
        )
    # feature surfing
        surfing_yes = 1
        surfing = st.toggle("Surfing",
                                 value=bool(surfing_yes)
        )
    # feature Jungle View
        jungleview_yes = 1
        jungle_view = st.toggle("Jungle View",
                                 value=bool(jungleview_yes)
        )
    # feature Island life
        islandlife_yes = 1
        islandlife = st.toggle("Island Life",
                                 value=bool(islandlife_yes)
        )
    # feature guest house
        guest_house_yes = 1
        guest_house = st.toggle("Guest House",
                                 value=bool(guest_house_yes)
        )

    with col3:
        # feature rice paddy view
            ricepaddyview_yes = 1
            rice_paddy_view = st.toggle("Rice Paddy View",
                                     value=bool(ricepaddyview_yes)
            )
        # feature Tropical
            tropical_yes = 1
            tropical = st.toggle("Tropical",
                                     value=bool(tropical_yes)
            )
        # feature Ocean View
            oceanview_yes = 1
            ocean_view = st.toggle("Ocean View",
                                     value=bool(oceanview_yes)
            )
        # feature Beachfront
            beachfront_yes = 1
            beachfront = st.toggle("Beach Front",
                                     value=bool(beachfront_yes)
            )
        # feature Golfing
            golfing_yes = 1
            golfing = st.toggle("Golfing",
                                     value=bool(golfing_yes)
            )
        # feature Amazing View
            amazing_view_yes = 1
            amazing_view = st.toggle("Golfing",
                                     value=bool(amazing_view_yes)
            )
          #Calling the model and scaler
          data = [bedrooms, bathrooms, agency, city, area, number_of_guests,
                  amazing_pool, pool_view, surfing, jungle_view, islandlife, guest_house,
                  rice_paddy_view, tropical, ocean_view, beachfront, golfing, amazing_view]
        
          with open("scaler.pkl", "rb") as scaler:
              scaler = pickle.load(scaler)
          with open("model.pkl", "rb") as model:
              model = pickle.load(model)
              
          columns=['bedrooms', 'bathrooms', 'agency', 'city', 'area', 'number_of_guests',
                   'Amazing pool', 'Pool view', 'Surfing', 'Jungle View', 'Island life','Guest House',
                   'Rice paddy view', 'Tropical', 'Ocean view','Beachfront', 'Golfing', 'Amazing View']
      
          input_data_df = pd.DataFrame([data], columns=columns)
      
          std_data = scaler.transform(input_data_df)
      
          prediction = model.predict(std_data)
      #prediction
        if st.button('Predict'):
            if None in data:
                st.markdown(':red[Please select/input correct data.]')
            else:
                st.write(f'Predicted Hotel Rental: {prediction[0].round(2)} $')





  
