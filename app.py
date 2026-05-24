import streamlit as st
import streamlit_authenticator as stauth

# --- CONFIGURATION ---
# Naye version ke mutabiq dictionary structure
config = {
    'credentials': {
        'usernames': {
            'qaisar': {
                'name': 'Qaisar Nadeem',
                'password': '$2b$12$R.S2.5fS05W7oQ.W.y17nOfp.9kXkP5bW0eXyR0C.N1F0uWJ6W89i'
            }
        }
    },
    'cookie': {
        'name': 'qaisar_cookie',
        'key': 'secret_key',
        'expiry_days': 30
    }
}

# Authenticator setup
authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days']
)

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
