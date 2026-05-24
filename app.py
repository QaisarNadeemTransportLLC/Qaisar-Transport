import streamlit as st
import streamlit_authenticator as stauth

# --- CUSTOM CSS ---
st.markdown("""
    <style>
    [data-testid="stSidebar"] { background-color: #FAF5F1; }
    div.stButton > button {
        width: 230px !important;
        height: 55px !important;
        background-color: #24388F !important;
        color: #ffffff !important;
        border: 1px solid #3d3d5c !important;
        border-radius: 8px !important;
        font-weight: 600 !important;
        font-size: 16px !important;
        margin-bottom: 10px !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
    }
    div.stButton > button:hover {
        background-color: #ff9f43 !important;
        color: white !important;
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
    
    if st.sidebar.button("Basic Info"): st.session_state.menu = "Basic Info"
    if st.sidebar.button("Labour Kharcha"): st.session_state.menu = "Labour Kharcha"
    if st.sidebar.button("Maintenance"): st.session_state.menu = "Maintenance"
    if st.sidebar.button("New Bill"): st.session_state.menu = "New Bill"
    if st.sidebar.button("Trips"): st.session_state.menu = "Trips"
    if st.sidebar.button("Coustomer List"): st.session_state.menu = "Coustomer List"
    if st.sidebar.button("Fines List"): st.session_state.menu = "Fines List"
    
    st.sidebar.markdown("---")
    if st.sidebar.button("Logout"): authenticator.logout("Logout", "main")

    # --- MAIN CONTENT LOGIC ---
    st.title(st.session_state.menu)

    if st.session_state.menu == "Basic Info":
        st.subheader("Add Driver and Vehicle Details")
        with st.form("driver_vehicle_form"):
            col1, col2 = st.columns(2)
            with col1:
                driver_name = st.text_input("Driver Name")
                license_no = st.text_input("License Number")
            with col2:
                vehicle_plate = st.text_input("Plate Number")
                model = st.text_input("Truck Model")
            
            if st.form_submit_button("Save Information"):
                st.success(f"Record saved for {driver_name}!")

    elif st.session_state.menu == "Labour Kharcha":
        st.write("Labour kharche ki details yahan add karein...")
    
    else:
        st.write(f"Abhi {st.session_state.menu} ka section under construction hai.")

elif authentication_status == False:
    st.error('Username/password is incorrect')
