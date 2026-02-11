import streamlit as st
import urllib.parse

# Configuration pour smartphone
st.set_page_config(page_title="Beauty Manager Pro", page_icon="✨")

# Design Luxe Noir et Or
st.markdown("""
    <style>
    .main { background-color: #000000; color: #D4AF37; }
    .stButton>button { background-color: #D4AF37; color: black; border-radius: 15px; width: 100%; font-weight: bold; border: none; height: 3.5rem; }
    .stSelectbox label, .stNumberInput label, .stTextInput label { color: #D4AF37 !important; font-weight: bold; }
    h1 { color: #D4AF37; text-align: center; font-family: 'Playfair Display', serif; }
    .stTabs [data-baseweb="tab-list"] { background-color: #000000; }
    .stTabs [data-baseweb="tab"] { color: white; border-radius: 10px 10px 0 0; }
    .stTabs [aria-selected="true"] { color: #D4AF37 !important; border-bottom-color: #D4AF37 !important; }
    div[data-testid="stExpander"] { background-color: #1a1a1a; border: 1px solid #D4AF37; border-radius: 10px; }
    </style>
    """, unsafe_allow_html=True)

st.title("💎 BEAUTY MANAGER PRO")
st.markdown("<p style='text-align: center; color: white;'>L'assistant des indépendantes de prestige</p>", unsafe_allow_html=True)

# Menu par onglets
tab1, tab2, tab3 = st.tabs(["💸 Encaisser", "📦 Catalogue", "📑 Reçu Express"])

# --- ONGLET 1 : ENCAISSEMENT ---
with tab1:
    st.subheader("Enregistrer une prestation")
    metier = st.selectbox("Votre spécialité", ["Coiffure & Perruques", "Onglerie", "Optique & Regard"])
    service = st.text_input("Nom du service (ex: Pose de perruque, Remplissage...)")
    prix = st.number_input("Montant de la prestation (€)", min_value=0)
    
    if st.button("✨ VALIDER LA VENTE"):
        st.balloons()
        st.success(f"Vente enregistrée : {service} - {prix}€")

# --- ONGLET 2 : CATALOGUE ---
with tab2:
    st.subheader("Mes Services & Tarifs")
    
    with st.expander("💇‍♀️ Coiffure & Perruques"):
        st.write("- Pose classique : 50€")
        st.write("- Customisation : 30€")
        st.write("- Soin profond : 45€")
        
    with st.expander("💅 Onglerie"):
        st.write("- Pose complète : 60€")
        st.write("- Remplissage : 40€")
        st.write("- Nail Art (par ongle) : 2€")
        
    with st.expander("👓 Optique & Regard"):
        st.write("- Examen de vue : Offert")
        st.write("- Pose de cils : 70€")

# --- ONGLET 3 : REÇU EXPRESS ---
with tab3:
    st.subheader("Envoyer un justificatif")
    st.write("Créez un message prêt à envoyer à votre cliente par SMS ou WhatsApp.")
    
    c_nom = st.text_input("Nom de la cliente")
    c_service = st.text_input("Service rendu")
    c_prix = st.number_input("Prix payé (€)", key="recu_prix")
    
    if st.button("📱 GÉNÉRER LE MESSAGE"):
        message_brut = f"Bonjour {c_nom}, merci pour votre visite chez Beauty Prestige ! ✨\n\nRécapitulatif :\n- Service : {c_service}\n- Total : {c_prix}€\n\nÀ très bientôt !"
        message_encode = urllib.parse.quote(message_brut)
        
        st.info("Copiez le texte ci-dessous ou cliquez sur le lien :")
        st.code(message_brut)
        st.markdown(f"[Envoyer via WhatsApp](https://wa.me/?text={message_encode})")

st.write("---")
st.caption("© 2026 Beauty Prestige Manager - Pour les pro de la beauté.")






