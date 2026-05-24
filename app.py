import streamlit as st

st.set_page_config(page_title="Qaisar Transport", layout="wide")

st.title("Qaisar Nadeem Transport LLC")
st.subheader("Fleet Management Dashboard")

# Navigation Menu
menu = st.sidebar.radio("Navigation", ["Home", "Add Trip", "Vehicle Expense"])

if menu == "Home":
    st.write("Welcome to your professional dashboard!")
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Income", "AED 0")
    col2.metric("Total Expenses", "AED 0")
    col3.metric("Net Profit", "AED 0")

elif menu == "Add Trip":
    st.header("Add New Trip")
    date = st.date_input("Date")
    amount = st.number_input("Amount")
    if st.button("Save Trip"):
        st.success("Trip Saved!")