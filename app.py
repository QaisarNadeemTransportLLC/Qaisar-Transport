import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader

# --- CONFIGURATION ---
# Hum password ko ab manual hash karenge taake error na aaye
names = ['Qaisar Nadeem']
usernames = ['qaisar']
# Note: 'admin123' ka hash ye hai
hashed_passwords = ['$2b$12$R.S2.5fS05W7oQ.W.y17nOfp.9kXkP5bW0eXyR0C.N1F0uWJ6W89i']

# Authentication setup
authenticator = stauth.Authenticate(
    names=names,
    usernames=usernames,
    hashed_passwords=hashed_passwords,
    cookie_name='qaisar_cookie',
    key='secret_key',
    cookie_expiry_days=30
)

# Login UI
name, authentication_status, username = authenticator.login('Login', 'main')

if authentication_status:
    st.title("Qaisar Nadeem Transport LLC")
    st.sidebar.title(f"Welcome {name}")
    
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
