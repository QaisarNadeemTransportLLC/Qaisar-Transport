import streamlit as st
import streamlit_authenticator as stauth

# --- CONFIGURATION ---
names = ['Qaisar Nadeem']
usernames = ['qaisar']
passwords = ['admin123']

# Hash passwords automatically for the library
hashed_passwords = stauth.Hasher(passwords).generate()

# Authentication setup (Version 0.3.x compatible)
authenticator = stauth.Authenticate(names, usernames, hashed_passwords,
    'qaisar_cookie', 'secret_key')

# Login UI
name, authentication_status, username = authenticator.login('Login', 'main')

if authentication_status:
    # --- DASHBOARD KA CODE YAHAN RAKHEIN ---
    st.title("Qaisar Nadeem Transport LLC")
    st.sidebar.title(f"Welcome {name}")
    
    # Ye raha aapka Basic Info section
    menu = ["Dashboard", "Basic Info"]
    choice = st.sidebar.selectbox("Navigation", menu)

    if choice == "Basic Info":
        st.subheader("Add Driver and Vehicle Details")
        st.write("Aapka form yahan aayega...")

    if st.sidebar.button('Logout'):
        authenticator.logout('Logout', 'main')

elif authentication_status == False:
    st.error('Username/password is incorrect')
elif authentication_status == None:
    st.warning('Please enter your username and password')
