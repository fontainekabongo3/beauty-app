import streamlit as st

st.set_page_config(page_title="Beauty Prestige", page_icon="💎")

# Style Luxe Noir et Or
st.markdown("""
    <style>
    .main { background-color: #000000; color: #D4AF37; }
    .stButton>button { background-color: #D4AF37; color: black; border-radius: 20px; width: 100%; }
    h1, h2, h3 { color: #D4AF37; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

st.title("💎 BEAUTY PRESTIGE")
st.write("### Gestion de Luxe")

tab1, tab2 = st.tabs(["🛒 Ventes", "📦 Produits"])

with tab1:
    st.subheader("Enregistrer une vente")
    service = st.selectbox("Prestation", ["Perruque", "Onglerie", "Maquillage"])
    prix = st.number_input("Montant (€)", min_value=0)
    if st.button("Valider la vente"):
        st.success(f"Vente de {service} ({prix}€) enregistrée !")

with tab2:
    st.subheader("Catalogue")
    st.info("Espace catalogue bientôt disponible.")



