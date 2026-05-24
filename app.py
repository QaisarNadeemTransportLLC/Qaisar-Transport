import streamlit as st
import streamlit_authenticator as stauth

# --- CUSTOM CSS FOR RICH PROFESSIONAL LOOK ---
st.markdown("""
    <style>
    /* Radio buttons ke gol circles (indicators) ko chhupa do */
    div[role="radiogroup"] input[type="radio"] {
        display: none;
    }
    
    /* Buttons ki styling */
    div[role="radiogroup"] > label {
        display: flex !important;
        justify-content: center !important;
        align-items: center !important;
        width: 100% !important;
        height: 50px !important;
        background-color: #2b2b40 !important;
        color: #ffffff !important;
        font-weight: bold !important;
        border-radius: 10px !important;
        margin-bottom: 8px !important;
        border: 1px solid #3d3d5c !important;
        transition: 0.3s !important;
        cursor: pointer;
    }
    
    /* Hover effect */
    div[role="radiogroup"] > label:hover {
        background-color: #3d3d5c !important;
    }
    
    /* Select hone par active style */
    div[role="radiogroup"] > label[data-checked="true"] {
        background-color: #ff9f43 !important;
        color: white !important;
        border: 2px solid #ff9f43 !important;
    }
    
    /* Sidebar ka background aur text */
    [data-testid="stSidebar"] {
        background-color: #1e1e2d;
    }
    </style>
""", unsafe_allow_html=True)

# --- CONFIGURATION ---
config = {
    'credentials': {
        'usernames': {
            'ehsan': {'name': 'Ehsan Sohna Jatt', 'password': stauth.Hasher(['Ehsan123']).generate()[0]},
            'qaisar': {'name': 'Qaisar Nadeem', 'password': stauth.Hasher(['admin123']).generate()[0]}
        }
    },
    'cookie': {'name': 'qaisar_cookie', 'key': 'secret_key', 'expiry_days': 30}
}

authenticator = stauth.Authenticate(config['credentials'], config['cookie']['name'], config['cookie']['key'], config['cookie']['expiry_days'])

# Login UI
name, authentication_status, username = authenticator.login('Login', 'main')

if authentication_status:
    st.sidebar.title(f"Welcome, {name}")
    
    # Navigation
    menu_items = [
        "Basic Info", "Labour Kharcha", "Maintenance", "New Bill", 
        "Trips", "Print Trip", "Labour", "Coustomers", "Fines List"
    ]
    
    choice = st.sidebar.radio("Navigation", menu_items)
    
    # --- NAVIGATION CONTENT ---
    if choice == "Basic Info":
        st.subheader("Basic Info: Driver & Vehicle Details")
        st.write("Yahan aap apne Drivers aur Vehicles ka record manage kar sakte hain.")
    elif choice == "Labour Kharcha":
        st.subheader("Labour Kharcha Management")
    elif choice == "Maintenance":
        st.subheader("Vehicle Maintenance Logs")
    elif choice == "New Bill":
        st.subheader("Generate New Bill")
    elif choice == "Trips":
        st.subheader("Daily Trip Management")
    elif choice == "Print Trip":
        st.subheader("Print Trip Reports")
    elif choice == "Labour":
        st.subheader("Labour Details")
    elif choice == "Coustomers":
        st.subheader("Customer Records")
    elif choice == "Fines List":
        st.subheader("Fines & Penalty List")

    st.sidebar.markdown("---")
    if st.sidebar.button('Logout'):
        authenticator.logout('Logout', 'main')

elif authentication_status == False:
    st.error('Username/password is incorrect')
elif authentication_status == None:
    st.warning('Please enter your username and password')
