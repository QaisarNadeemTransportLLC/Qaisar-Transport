import streamlit as st
import streamlit_authenticator as stauth

# --- CONFIGURATION ---
names = ['Qaisar Nadeem']
usernames = ['qaisar']
# Yeh wahi password 'admin123' ka hash hai
hashed_passwords = ['$2b$12$R.S2.5fS05W7oQ.W.y17nOfp.9kXkP5bW0eXyR0C.N1F0uWJ6W89i']

# Simple Authenticator Setup
authenticator = stauth.Authenticate(names, usernames, hashed_passwords, 'qaisar_cookie', 'secret_key')

# Login UI
name, authentication_status, username = authenticator.login('Login', 'main')

if authentication_status:
    st.title("Qaisar Nadeem Transport LLC")
    st.sidebar.write(f"Welcome {name}")
    
    # Navigation
    choice = st.sidebar.selectbox("Navigation", ["Dashboard", "Basic Info"])
    
    if choice == "Basic Info":
        st.subheader("Add Driver and Vehicle Details")
        st.write("Ab aap yahan apna form shuru kar sakte hain.")

    if st.sidebar.button('Logout'):
        authenticator.logout('Logout', 'main')

elif authentication_status == False:
    st.error('Username/password is incorrect')
elif authentication_status == None:
    st.warning('Please enter your username and password')
