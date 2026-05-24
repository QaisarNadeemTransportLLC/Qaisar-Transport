import streamlit as st
import streamlit_authenticator as stauth

# --- CONFIGURATION ---
# Yahan aap jitne marzi users add kar sakte hain
config = {
    'credentials': {
        'usernames': {
            'ehsan': {
                'name': 'Ehsan Sohna Jatt',
                'password': stauth.Hasher(['Ehsan123']).generate()[0]
            },
            'qaisar': {
                'name': 'Qaisar Nadeem',
                'password': stauth.Hasher(['admin123']).generate()[0]
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
    
    # Navigation Buttons (Sidebar mein)
    st.sidebar.title("Navigation")
    choice = st.sidebar.radio("Select Option", [
        "Basic Info", 
        "Labour Kharcha", 
        "Maintenance", 
        "New Bill", 
        "Trips", 
        "Print Trip", 
        "Labour", 
        "Coustomers", 
        "Fines List"
    ])

    # Ab ye check karega ke aapne kaunsa button dabaya hai
    if choice == "Basic Info":
        st.subheader("Add Driver and Vehicle Details")
        # Yahan aap apna form ka code dalenge...
        
    elif choice == "Labour Kharcha":
        st.subheader("Labour Kharcha Section")
        
    elif choice == "Maintenance":
        st.subheader("Maintenance Section")
    
    # Isi tarah baaki sections bhi ban jayenge...
    
    if choice == "Basic Info":
        st.subheader("Add Driver and Vehicle Details")
        st.write("Ab aap yahan apna form shuru kar sakte hain.")

    if st.sidebar.button('Logout'):
        authenticator.logout('Logout', 'main')

elif authentication_status == False:
    st.error('Username/password is incorrect')
elif authentication_status == None:
    st.warning('Please enter your username and password')
