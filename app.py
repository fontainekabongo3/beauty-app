import streamlit as st

st.set_page_config(page_title="Beauty Prestige", page_icon="💎")

# Style Luxe Noir et Or
st.markdown("""
    <style>
    .main { background-color: #000000; color: #D4AF37; }
    .stButton>button { background-color: #D4AF37; color: black; border-radius: 20px; }
    h1, h2, h3 { color: #D4AF37; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

st.title("💎 BEAUTY PRESTIGE MANAGER")
st.write("Bienvenue dans votre espace de gestion luxe.")

tab1, tab2 = st.tabs(["🛒 Encaissement", "📦 Catalogue"])

with tab1:
    st.subheader("Nouvelle Vente")
    service = st.selectbox("Prestation", ["Perruque", "Onglerie", "Maquillage"])
    prix = st.number_input("Montant (€)", min_value=0)
    if st.button("Valider la vente"):
        st.success(f"Vente de {service} ({prix}€) enregistrée localement !")

with tab2:
    st.subheader("Nos Produits")
    st.info("Le catalogue est en cours de mise à jour.")


