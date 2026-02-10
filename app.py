import streamlit as st
from supabase import create_client, Client

# --- CONFIGURATION SUPABASE ---
URL = st.secrets["SUPABASE_URL"]
KEY = st.secrets["SUPABASE_KEY"]
supabase: Client = create_client(URL, KEY)

# --- STYLE ET DESIGN (DISAINE) ---
st.markdown("""
    <style>
    .main { 
        background-color: #0e1117; 
        color: #f5f5f5; 
        font-family: 'Montserrat', sans-serif;
    }
    .stButton>button { 
        background-color: #D4AF37; 
        color: black; 
        border-radius: 20px; 
        font-weight: bold; 
        width: 100%;
        margin-top: 15px;
        padding: 10px 20px;
        border: none;
    }
    .card {
        padding: 20px; 
        border-radius: 15px;
        background-color: #1c1c1c; 
        border: 1px solid #D4AF37;
        margin-bottom: 15px;
        box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2);
    }
    h1, h2, h3 { 
        color: #D4AF37; 
        text-align: center; 
        font-family: 'Playfair Display', serif;
    }
    .stTextInput>div>div>input, .stSelectbox>div>div>select, .stNumberInput>div>div>input {
        background-color: #2a2a2a;
        color: #f5f5f5;
        border: 1px solid #444444;
        border-radius: 8px;
        padding: 10px;
    }
    .stTabs [data-baseweb="tab-list"] button [data-testid="stMarkdownContainer"] p {
        font-size: 1.1rem;
        color: #D4AF37;
    }
    .stTabs [data-baseweb="tab-list"] {
        gap: 24px;
    }
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        white-space: nowrap;
        border-bottom: 1px solid #444444;
    }
    .stTabs [aria-selected="true"] {
        border-bottom: 3px solid #D4AF37;
    }
    </style>
    <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&family=Playfair+Display:wght@700&display=swap" rel="stylesheet">
    """, unsafe_allow_html=True)


# --- OPTIONS DE LANGUES ---
lang = st.sidebar.selectbox("🌐 Language / Langue", ["Français", "English"])

# Dictionnaire pour les traductions
translations = {
    "Français": {
        "title": "💎 Beauty Pro Manager",
        "welcome": "Bienvenue !",
        "client_name": "Nom de la cliente",
        "service_type": "Prestation",
        "total_price": "Prix total (€)",
        "deposit_paid": "Acompte versé (€)",
        "record_sale": "Valider et Enregistrer",
        "sale_recorded_success": "✅ enregistré pour {name} !",
        "new_entry": "💸 Nouvel Encaissement",
        "history_tab": "📜 Historique",
        "catalog_tab": "📸 Styles & Produits",
        "afro_styles": "Coupes & Styles Afro",
        "nails_colors": "Vernis & Couleurs",
        "products_care": "Produits & Soins",
        "total": "Total",
        "deposit": "Acompte",
        "remaining": "Reste à payer",
        "search_client": "Rechercher une cliente...",
        "no_sales": "Aucune vente enregistrée pour le moment.",
        "search_placeholder": "Rechercher par nom de cliente..."
    },
    "English": {
        "title": "💎 Beauty Pro Manager",
        "welcome": "Welcome!",
        "client_name": "Client Name",
        "service_type": "Service Type",
        "total_price": "Total Price (€)",
        "deposit_paid": "Deposit Paid (€)",
        "record_sale": "Validate and Record",
        "sale_recorded_success": "✅ recorded for {name}!",
        "new_entry": "💸 New Entry",
        "history_tab": "📜 History",
        "catalog_tab": "📸 Styles & Products",
        "afro_styles": "Afro Cuts & Styles",
        "nails_colors": "Nails & Colors",
        "products_care": "Products & Care",
        "total": "Total",
        "deposit": "Deposit",
        "remaining": "Remaining",
        "search_client": "Search client...",
        "no_sales": "No sales recorded yet.",
        "search_placeholder": "Search by client name..."
    }
}
t = translations[lang] # Sélectionne la traduction actuelle

# --- LOGO & TITRE ---
st.markdown(f"<div style='text-align: center;'>", unsafe_allow_html=True)
# Remplace l'URL ci-dessous par celle de ton LOGO PERSONNALISÉ
st.image("https://img.icons8.com/color/100/diamond--v1.png", width=100) 
st.markdown(f"<h1>{t['title']}</h1>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# --- NAVIGATION AVEC ONGLETS ---
tab1, tab2, tab3 = st.tabs([t["new_entry"], t["catalog_tab"], t["history_tab"]])

# --- ONGLET 1 : NOUVEL ENCAISSEMENT ---
with tab1:
    st.markdown(f"<div class='card'>", unsafe_allow_html=True)
    name = st.text_input(t["client_name"], placeholder=t["search_client"])
    service = st.selectbox(t["service_type"], ["Tresses", "Locks", "Défrisage", "Soin Profond", "Pose Vernis", "Autre"])
    
    col_price, col_deposit = st.columns(2)
    price = col_price.number_input(t["total_price"], min_value=0.0, format="%.2f")
    deposit = col_deposit.number_input(t["deposit_paid"], min_value=0.0, max_value=price, format="%.2f")
    
    if st.button(t["record_sale"]):
        data = {"nom_client": name, "prestation": service, "prix": price, "acompte": deposit}
        supabase.table("ventes").insert(data).execute()
        st.success(t["sale_recorded_success"].format(name=name))
    st.markdown("</div>", unsafe_allow_html=True)

# --- ONGLET 2 : CATALOGUE VISUEL (IMAGES PERSONNALISABLES) ---
with tab2:
    st.header(t["afro_styles"])
    col_a1, col_a2 = st.columns(2)
    # Remplacer les URL des images ci-dessous par les tiennes
    with col_a1:
        st.image("https://images.unsplash.com/photo-1594916892607-e8156106606d?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=400&q=80", caption="Tresses Box Braids")
        st.image("https://images.unsplash.com/photo-1621644781708-590b1e3e7f91?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=400&q=80", caption="Coiffure Nattes")
    with col_a2:
        st.image("https://images.unsplash.com/photo-1614397782354-f89a87d0e9b2?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=400&q=80", caption="Locks Élégantes")
        st.image("https://images.unsplash.com/photo-1563232049-74d6f83d9b07?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=400&q=80", caption="Twists Modernes")

    st.header(t["nails_colors"])
    # Remplacer les URL des images ci-dessous par les tiennes
    st.image("https://images.unsplash.com/photo-1604928031362-e565363404c0?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=800&q=80", caption="Collection de Vernis")

    st.header(t["products_care"])
    # Remplacer les URL des images ci-dessous par les tiennes
    st.image("https://images.unsplash.com/photo-1596462502278-27ddab0c867e?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=800&q=80", caption="Gamme de Soins Capillaires")


# --- ONGLET 3 : HISTORIQUE (Avec recherche et calcul) ---
with tab3:
    st.header(t["history_tab"])
    
    search_query = st.text_input(t["search_placeholder"], key="search_history")
    
    res = supabase.table("ventes").select("*").order("created_at", desc=True).execute()
    
    filtered_data = []
    total_sales_month = 0.0
    
    if res.data:
        for v in res.data:
            # Filtrer par recherche
            if search_query.lower() in v['nom_client'].lower():
                filtered_data.append(v)
            
            # Calculer les ventes du mois (à adapter si besoin pour un mois spécifique)
            # Pour l'exemple, on prend toutes les ventes
            if v['prix']: # S'assurer que 'prix' n'est pas vide
                total_sales_month += float(v['prix'])

        if not filtered_data:
            st.info(t["no_sales"])
        else:
            st.subheader(f"Total des ventes: {total_sales_month:.2f}€") # Affiche le total
            for v in filtered_data:
                reste_a_payer = float(v['prix']) - float(v['acompte'])
                st.markdown(f"""
                <div class='card'>
                    <b>{v['nom_client']}</b> - {v['prestation']}<br>
                    🗓️ {v['created_at'].split('T')[0]}<br>
                    💰 {t['total']}: {v['prix']:.2f}€ | ✨ {t['deposit']}: {v['acompte']:.2f}€ | 🔴 {t['remaining']}: {reste_a_payer:.2f}€
                </div>
                """, unsafe_allow_html=True)
    else:
        st.info(t["no_sales"])


