import streamlit as st
import urllib.parse

st.set_page_config(page_title="Beauty Pro", page_icon="✨")

# DESIGN INSPIRÉ DE WIX (CLAIR, PROFESSIONNEL, CHIC)
st.markdown("""
    <style>
    /* Fond gris perle très clair */
    .main { background-color: #FDFCFB; color: #4A4A4A; }
    
    /* Boutons arrondis couleur Rose Gold / Sable */
    .stButton>button { 
        background-color: #D4B9A8; 
        color: white; 
        border-radius: 25px; 
        border: none;
        height: 3.5rem;
        font-weight: 300;
        letter-spacing: 1px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        transition: 0.3s;
    }
    .stButton>button:hover { background-color: #C4A694; border: none; color: white; }

    /* Titres élégants */
    h1 { color: #8E735B; font-family: 'serif'; font-weight: 400; text-align: center; }
    h3 { color: #A88B73; font-weight: 300; }
    
    /* Onglets modernes */
    .stTabs [data-baseweb="tab-list"] { background-color: transparent; }
    .stTabs [data-baseweb="tab"] { color: #9B9B9B; font-size: 16px; }
    .stTabs [aria-selected="true"] { color: #8E735B !important; border-bottom-color: #8E735B !important; }
    
    /* Encadrés pour le stock et les calculs */
    div[data-testid="stExpander"] { 
        background-color: white; 
        border: 1px solid #F0E6E0; 
        border-radius: 15px; 
    }
    </style>
    """, unsafe_allow_html=True)

st.title("✨ BEAUTY ASSISTANT")
st.markdown("<p style='text-align: center; color: #9B9B9B; font-style: italic;'>L'élégance au service de votre gestion</p>", unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(["💎 Encaissement", "📊 Calculs & Monnaie", "📩 Reçu Client"])

with tab1:
    st.subheader("Nouvelle Vente")
    col1, col2 = st.columns(2)
    with col1:
        service = st.selectbox("Prestation", ["Coiffure", "Ongles", "Regard", "Autre"])
    with col2:
        prix = st.number_input("Prix (€)", min_value=0)
    
    if st.button("ENREGISTRER LA PRESTATION"):
        st.success(f"Validé avec succès : {service} ({prix}€)")

with tab2:
    st.subheader("Calculatrice de Restitution")
    t_du = st.number_input("Montant total à payer", min_value=0)
    t_recu = st.number_input("Montant donné par la cliente", min_value=0)
    if t_recu > 0:
        reste = t_recu - t_du
        if reste >= 0:
            st.metric("À RENDRE :", f"{reste} €")
        else:
            st.error(f"Attention, il manque {-reste} €")

with tab3:
    st.subheader("Envoyer un Reçu WhatsApp")
    nom = st.text_input("Prénom de la cliente")
    if st.button("GÉNÉRER LE MESSAGE PRO"):
        msg = f"Bonjour {nom}, c'est Beauty Prestige ! ✨ Votre règlement de {prix}€ a bien été pris en compte. Merci de votre confiance."
        link = f"https://wa.me/?text={urllib.parse.quote(msg)}"
        st.markdown(f"[📲 Cliquer ici pour envoyer le message]({link})")







