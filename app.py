import streamlit as st

# Configuration de la page
st.set_page_config(page_title="Beauty Prestige", page_icon="💎")

# Style Luxe Noir et Or
st.markdown("""
    <style>
    .main { background-color: #000000; color: #D4AF37; }
    .stButton>button { background-color: #D4AF37; color: black; border-radius: 20px; width: 100%; font-weight: bold; }
    h1, h2, h3 { color: #D4AF37; text-align: center; }
    p { color: white; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

st.title("💎 BEAUTY PRESTIGE")
st.write("Gestionnaire de Ventes Privé")

# Création des onglets
tab1, tab2 = st.tabs(["🛒 Encaisser", "📦 Catalogue"])

with tab1:
    st.subheader("Nouvelle Vente")
    service = st.selectbox("Prestation", ["Perruque", "Onglerie", "Maquillage"])
    prix = st.number_input("Montant (€)", min_value=0)
    if st.button("Enregistrer la vente"):
        st.success(f"Vente de {service} ({prix}€) validée !")

with tab2:
    st.subheader("Catalogue Produits")
    st.info("Espace de consultation des stocks.")




