import streamlit as st
import pandas as pd

# 1. Configuration Style Luxe
st.set_page_config(page_title="Beauty Pro Manager", page_icon="✨", layout="centered")

# CSS pour personnaliser les couleurs (Or et Blanc)
st.markdown("""
    <style>
    .main { background-color: #ffffff; }
    .stButton>button { width: 100%; border-radius: 20px; background-color: #D4AF37; color: white; border: none; font-weight: bold; }
    .stTextInput>div>div>input { border-radius: 10px; }
    h1 { color: #2C3E50; font-family: 'Helvetica'; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

# 2. Système de Connexion
if 'auth' not in st.session_state:
    st.session_state.auth = False

def login():
    st.title("🔑 Accès Privé")
    st.write("Veuillez vous connecter pour gérer votre salon.")
    user = st.text_input("Identifiant")
    password = st.text_input("Mot de passe", type="password")
    if st.button("Se connecter"):
        if user == "admin" and password == "1234":
            st.session_state.auth = True
            st.rerun()
        else:
            st.error("Identifiants incorrects. Indice : admin / 1234")

# 3. Application Principale (Visible seulement si connecté)
if not st.session_state.auth:
    login()
else:
    # Barre latérale de navigation
    with st.sidebar:
        st.title("💎 Menu")
        page = st.radio("Navigation", ["Tableau de Bord", "Gestion des Stocks"])
        st.divider()
        if st.button("Déconnexion"):
            st.session_state.auth = False
            st.rerun()

    if page == "Tableau de Bord":
        st.title("✨ Mon Dashboard")
        
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Ventes du jour", "120 €")
        with col2:
            st.metric("Relances à faire", "4")

        st.divider()
        st.subheader("💰 Nouvel Encaissement")
        nom = st.text_input("Nom de la cliente", placeholder="Ex: Sarah")
        montant = st.number_input("Montant de la prestation (€)", min_value=0, step=5)
        
        if st.button("Valider et Enregistrer"):
            st.balloons()
            st.success(f"Vente de {montant}€ enregistrée pour {nom} !")

    elif page == "Gestion des Stocks":
        st.title("📦 Mes Stocks")
        st.info("Suivez l'utilisation de vos produits en temps réel.")
        
        # Exemple de stock simple
        items = {"Mèches (paquets)": 12, "Vernis semi-perm": 8, "Huile soin": 5}
        for item, qte in items.items():
            c1, c2 = st.columns([3, 1])
            c1.write(f"**{item}** : {qte} restants")
            if c2.button(f"Retirer 1", key=item):
                st.toast(f"Stock mis à jour pour {item}")
