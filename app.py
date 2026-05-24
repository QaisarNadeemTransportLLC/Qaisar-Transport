import streamlit as st
import streamlit_authenticator as stauth

# --- CUSTOM CSS FOR PREMIUM LOOK ---
st.markdown("""
    <style>
    [data-testid="stSidebar"] { background-color: #1e1e2d; }
    div.stButton > button {
        width: 100%;
        height: 50px;
        background-color: #2b2b40 !important;
        color: white !important;
        border: 1px solid #3d3d5c !important;
        border-radius: 10px !important;
        font-weight: bold !important;
        margin-bottom: 8px !important;
    }
    div.stButton > button:hover {
        background-color: #ff9f43 !important;
        border: 1px solid #ff9f43 !important;
    }
    </style>
""", unsafe_allow_html=True)

# --- AUTH CONFIG ---
config = {
    'credentials': {'usernames': {
        'ehsan': {'name': 'Ehsan Sohna Jatt', 'password': stauth.Hasher(['Ehsan123']).generate()[0]},
        'qaisar': {'name': 'Qaisar Nadeem', 'password': stauth.Hasher(['admin123']).generate()[0]}
    }},
    'cookie': {'name': 'qaisar_cookie', 'key': 'secret_key', 'expiry_days': 30}
}
authenticator = stauth.Authenticate(config['credentials'], config['cookie']['name'], config['cookie']['key'], config['cookie']['expiry_days'])

name, authentication_status, username = authenticator.login('Login', 'main')

if authentication_status:
    if 'menu' not in st.session_state: st.session_state.menu = "Basic Info"

    st.sidebar.title(f"Welcome, {name}")
    
    # Buttons
    if st.sidebar.button("Basic Info"): st.session_state.menu = "Basic Info"
    if st.sidebar.button("Labour Kharcha"): st.session_state.menu = "Labour Kharcha"
    if st.sidebar.button("Maintenance"): st.session_state.menu = "Maintenance"
    if st.sidebar.button("New Bill"): st.session_state.menu = "New Bill"
    if st.sidebar.button("Trips"): st.session_state.menu = "Trips"
    
    st.sidebar.markdown("---")
    if st.sidebar.button("Logout"): authenticator.logout("Logout", "main")

    # Content
    st.title(st.session_state.menu)
    st.write(f"Ab aap {st.session_state.menu} par kaam kar rahe hain.")

elif authentication_status == False:
    st.error('Username/password is incorrect')
