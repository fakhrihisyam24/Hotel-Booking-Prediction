import streamlit as st
import pandas as pd
import pickle

# Load model
model_filename = "BEST_MODEL_for_hotel_booking_demand.pkl"
with open(model_filename, "rb") as model_file:
    model = pickle.load(model_file)

# Title
st.title("Hotel Booking Demand Prediction")

# Sidebar inputs
st.sidebar.header("Input Booking Details")

# Numerical Inputs
lead_time = st.sidebar.slider("Lead Time (days)", 0, 700, 30)
arrival_date_year = st.sidebar.selectbox("Arrival Year", [2015, 2016, 2017])
stays_in_weekend_nights = st.sidebar.slider("Weekend Nights", 0, 19, 1)
stays_in_week_nights = st.sidebar.slider("Week Nights", 0, 50, 3)
adults = st.sidebar.slider("Adults", 0, 4, 2)
children = st.sidebar.slider("Children", 0, 3, 0)
babies = st.sidebar.slider("Babies", 0, 2, 0)
previous_cancellations = st.sidebar.slider("Previous Cancellations", 0, 26, 0)
previous_bookings_not_canceled = st.sidebar.slider("Previous Non-Canceled Bookings", 0, 72, 0)
booking_changes = st.sidebar.slider("Booking Changes", 0, 18, 0)
days_in_waiting_list = st.sidebar.slider("Days in Waiting List", 0, 391, 0)
adr = st.sidebar.slider("Average Daily Rate (ADR)", 0.0, 510.0, 100.0)
required_car_parking_spaces = st.sidebar.slider("Car Parking Spaces", 0, 3, 0)
total_of_special_requests = st.sidebar.slider("Special Requests", 0, 5, 0)
arrival_date_week_number = st.sidebar.slider("Arrival Week Number", 1, 53, 20)
arrival_date_day_of_month = st.sidebar.slider("Arrival Day of Month", 1, 31, 15)

# Categorical Inputs
hotel = st.sidebar.selectbox("Hotel Type", ["Resort Hotel", "City Hotel"])
arrival_date_month = st.sidebar.selectbox("Arrival Month", [
    "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"
])
meal = st.sidebar.selectbox("Meal Type", ["BB", "FB", "HB", "SC"])
market_segment = st.sidebar.selectbox("Market Segment", ["Direct", "Corporate", "Online TA", "Offline TA/TO", "Groups", "Complementary", "Aviation"])
distribution_channel = st.sidebar.selectbox("Distribution Channel", ["Direct", "Corporate", "TA/TO", "GDS"])
reserved_room_type = st.sidebar.selectbox("Reserved Room Type", ["A", "C", "D", "E", "G", "F", "B", "H", "L"])
assigned_room_type = st.sidebar.selectbox("Assigned Room Type", ("C","A","D","E","G","F","B","H","I","K"))
deposit_type = st.sidebar.selectbox("Deposit Type", ["No Deposit", "Refundable", "Non Refund"])
customer_type = st.sidebar.selectbox("Customer Type", ["Transient", "Contract", "Transient-Party", "Group"])
reservation_status = st.sidebar.selectbox("Reservation Status", ["Check-Out", "Canceled", "No-Show"])

# Prepare input data
data = pd.DataFrame({
    "lead_time": [lead_time],
    "arrival_date_year": [arrival_date_year],
    "stays_in_weekend_nights": [stays_in_weekend_nights],
    "stays_in_week_nights": [stays_in_week_nights],
    "adults": [adults],
    "children": [children],
    "babies": [babies],
    "previous_cancellations": [previous_cancellations],
    "previous_bookings_not_canceled": [previous_bookings_not_canceled],
    "booking_changes": [booking_changes],
    "days_in_waiting_list": [days_in_waiting_list],
    "adr": [adr],
    "required_car_parking_spaces": [required_car_parking_spaces],
    "total_of_special_requests": [total_of_special_requests],
    "arrival_date_week_number": [arrival_date_week_number],
    "arrival_date_day_of_month": [arrival_date_day_of_month],
    "hotel": [hotel],
    "arrival_date_month": [arrival_date_month],
    "meal": [meal],
    "market_segment": [market_segment],
    "distribution_channel": [distribution_channel],
    "reserved_room_type": [reserved_room_type],
    "assigned_room_type": [assigned_room_type],
    "deposit_type": [deposit_type],
    "customer_type": [customer_type],
    "reservation_status": [reservation_status]
})

# Predict button
if st.button("Predict Booking Demand"):
    prediction = model.predict(data)
    st.subheader("Prediction Result:")
    st.write("Booking Status:", "Canceled" if prediction[0] == 1 else "Not Canceled")

exit()

