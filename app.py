import streamlit as st
import streamlit_authenticator as stauth

# --- CONFIGURATION ---
# Yahan apne login details rakhein
names = ['Qaisar Nadeem']
usernames = ['qaisar']
passwords = ['qaisar123'] # Apna password yahan change kar lein

# Password hashing (New Method)
hashed_passwords = stauth.Hasher(passwords).generate()

# Authentication setup
authenticator = stauth.Authenticate(names, usernames, hashed_passwords,
    'qaisar_cookie', 'secret_key')

# Login UI
name, authentication_status, username = authenticator.login()

if authentication_status:
    # --- YAHAN SE AAPKA DASHBOARD SHURU HOGA ---
    st.title("Qaisar Nadeem Transport LLC")
    st.write(f'Welcome back, {name}!')
    
    # Aapka original dashboard code yahan aayega
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Income", "AED 50,000")
    col2.metric("Total Expenses", "AED 12,000")
    col3.metric("Net Profit", "AED 38,000")
    
    authenticator.logout('Logout', 'main')

elif authentication_status == False:
    st.error('Username/password is incorrect')
elif authentication_status == None:
    st.warning('Please enter your username and password')
