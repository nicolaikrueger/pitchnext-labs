import streamlit as st

# Titel der Seite setzen
st.title('pitchnext Lab')

# Passwortabfrage
password = st.text_input("Bitte geben Sie das Passwort ein:", type="password")

# Überprüfung des Passworts
if password:
    # Zugriff auf das in Streamlit Secrets gespeicherte Passwort
    correct_password = st.secrets["app_password"]
    
    if password == correct_password:
        st.success("Passwort akzeptiert.")
        
        # Erstellung einer einfachen Navigationsleiste
        tab1, tab2, tab3 = st.tabs(["Hauptseite", "Seite 2", "Seite 3"])
        
        with tab1:
            st.header("Willkommen bei pitchnext Lab")
            st.write("Hier könnten weitere Informationen oder Funktionen präsentiert werden.")
        
        with tab2:
            st.header("Seite 2")
            st.write("Details oder Funktionen für Seite 2.")
        
        with tab3:
            st.header("Seite 3")
            st.write("Details oder Funktionen für Seite 3.")
        
    else:
        st.error("Falsches Passwort, bitte versuchen Sie es erneut!")
