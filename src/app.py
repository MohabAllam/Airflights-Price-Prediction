import streamlit as st
import joblib
from inference import make_prediction

html_title = """<h1 style="color:white;text-align:center;"> India Airflights Price Prediction </h1>"""
st.markdown(html_title, unsafe_allow_html=True)

# Load Unique Values
uniq_val_dict = joblib.load('metadata/unique_values_dict.pkl')

# Create Input Widgets
Airline = st.selectbox('Airline', uniq_val_dict['Airline'])
Source = st.selectbox('Source', uniq_val_dict['Source'])
Destination = st.selectbox('Destination', uniq_val_dict['Destination'])
journey_weekday = st.selectbox('journey_weekday', uniq_val_dict['journey_weekday'])
Dep_hour = st.selectbox('Dep_hour', uniq_val_dict['Dep_hour'])

journey_month = st.sidebar.slider('journey_month', min_value= uniq_val_dict['journey_month'].min(), max_value= uniq_val_dict['journey_month'].max(), step= 1)
journey_day = st.sidebar.slider('journey_day', min_value= uniq_val_dict['journey_day'].min(), max_value= uniq_val_dict['journey_day'].max(), step= 1)
Num_of_stops = st.sidebar.slider('Num_of_stops', min_value= uniq_val_dict['Num_of_stops'].min(), max_value= uniq_val_dict['Num_of_stops'].max(), step= 1)

Duration = st.number_input('Duration', min_value= uniq_val_dict['Duration'].min(), max_value= uniq_val_dict['Duration'].max())
distance = st.number_input('distance', min_value= uniq_val_dict['distance'].min(), max_value= uniq_val_dict['distance'].max())


# Make Prediction

if st.button('Predict'):

    result = make_prediction(Values= [Airline, Source, Destination, Duration, journey_month, journey_day,
                                      journey_weekday, Dep_hour, distance, Num_of_stops])
    
    st.write(result)