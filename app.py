import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader

# Credentials ka setup (Yahan apna username/password set karein)
names = ['Qaisar Nadeem']
usernames = ['qaisar']
passwords = ['admin123'] # Yahan apna password change kar lein

hashed_passwords = stauth.Hasher(passwords).generate()

authenticator = stauth.Authenticate(names, usernames, hashed_passwords,
    'some_cookie_name', 'some_signature_key', cookie_expiry_days=30)

name, authentication_status, username = authenticator.login('Login', 'main')

if authentication_status:
    # --- YAHAN SE AAPKA ASLI DASHBOARD KA CODE SHURU HOGA ---
    st.write(f'Welcome *{name}*')
    # Aapka baaki dashboard ka code yahan aayega...
    
    if st.button('Logout'):
        authenticator.logout('Logout', 'main')

elif authentication_status == False:
    st.error('Username/password is incorrect')
elif authentication_status == None:
    st.warning('Please enter your username and password')
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
