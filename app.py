import streamlit as st
from supabase import create_client, Client

# --- CONNEXION SUPABASE ---
URL = st.secrets["SUPABASE_URL"]
KEY = st.secrets["SUPABASE_KEY"]
supabase: Client = create_client(URL, KEY)

# --- STYLE LUXE NOIR & OR ---
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: #f5f5f5; font-family: 'Montserrat', sans-serif; }
    .stButton>button { 
        background-color: #D4AF37; color: black; border-radius: 25px; 
        font-weight: bold; width: 100%; border: none; padding: 12px;
    }
    .card {
        padding: 20px; border-radius: 15px; background-color: #1c1c1c; 
        border: 1px solid #D4AF37; margin-bottom: 15px;
    }
    h1, h2, h3 { color: #D4AF37; text-align: center; }
    .stTabs [data-baseweb="tab-list"] { gap: 10px; }
    .stTabs [data-baseweb="tab"] {
        color: #D4AF37; border-radius: 10px 10px 0 0; padding: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- TRADUCTIONS ---
lang = st.sidebar.selectbox("🌐 Langue / Language", ["Français", "English"])
t = {
    "Français": {
        "title": "BEAUTY PRESTIGE MANAGER",
        "tab1": "💸 Encaissement",
        "tab2": "📸 Catalogue",
        "tab3": "📜 Historique",
        "client": "Nom de la cliente",
        "service": "Prestation",
        "price": "Prix total (€)",
        "deposit": "Acompte versé (€)",
        "save": "Enregistrer la vente",
        "cat1": "Styles Afro & Tresses",
        "cat2": "Perruques & Lace",
        "cat3": "Onglerie & Vernis",
        "cat4": "Maquillage & Mariage",
        "total": "Total :",
        "remains": "Reste à payer :"
    },
    "English": {
        "title": "BEAUTY PRESTIGE MANAGER",
        "tab1": "💸 Checkout",
        "tab2": "📸 Catalog",
        "tab3": "📜 History",
        "client": "Client Name",
        "service": "Service",
        "price": "Total Price (€)",
        "deposit": "Deposit Paid (€)",
        "save": "Record Sale",
        "cat1": "Afro Styles & Braids",
        "cat2": "Wigs & Lace",
        "cat3": "Nails & Polish",
        "cat4": "Makeup & Wedding",
        "total": "Total:",
        "remains": "Remaining:"
    }
}[lang]

# --- HEADER ---
st.markdown(f"<h1>{t['title']}</h1>", unsafe_allow_html=True)
st.markdown("<div style='text-align:center'><img src='https://img.icons8.com/color/100/diamond--v1.png' width='60'></div>", unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs([t["tab1"], t["tab2"], t["tab3"]])

# --- ONGLET 1 : ENCAISSEMENT + ACOMPTE ---
with tab1:
    with st.container():
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        nom = st.text_input(t["client"])
        service = st.selectbox(t["service"], ["Box Braids", "Locks", "Tissage", "Perruque", "Manucure", "Maquillage Mariage", "Soin Capillaire"])
        c1, c2 = st.columns(2)
        poids = c1.number_input(t["price"], min_value=0)
        acompte = c2.number_input(t["deposit"], min_value=0)
        
        if st.button(t["save"]):
            data = {"nom_client": nom, "prestation": service, "prix": poids, "acompte": acompte}
            supabase.table("ventes").insert(data).execute()
            st.success(f"✨ {nom} enregistré !")
        st.markdown("</div>", unsafe_allow_html=True)

# --- ONGLET 2 : CATALOGUE DE LUXE ---
with tab2:
    # Section Coiffure
    st.subheader(t["cat1"])
    col1, col2 = st.columns(2)
    col1.image("http://googleusercontent.com/image_collection/image_retrieval/959625805647718726_2", caption="Box Braids Gold")
    col2.image("http://googleusercontent.com/image_collection/image_retrieval/14155844831748715597_1", caption="Premium Locks")

    # Section Wigs
    st.subheader(t["cat2"])
    col3, col4 = st.columns(2)
    col3.image("http://googleusercontent.com/image_collection/image_retrieval/4516411950141285414_0", caption="Lace Frontal Silk")
    col4.image("http://googleusercontent.com/image_collection/image_retrieval/8683863162794941081_2", caption="Human Hair Extensions")

    # Section Ongles & Maquillage
    st.subheader(t["cat3"])
    st.image("http://googleusercontent.com/image_collection/image_retrieval/1777215304990739670_2", caption="Palette Vernis Luxe")
    
    st.subheader(t["cat4"])
    st.image("http://googleusercontent.com/image_collection/image_retrieval/792672473451217764_1", caption="Mariage & Glow Makeup")

# --- ONGLET 3 : HISTORIQUE INTERACTIF ---
with tab3:
    res = supabase.table("ventes").select("*").order("created_at", desc=True).execute()
    if res.data:
        for v in res.data:
            reste = v['prix'] - v['acompte']
            color = "#D4AF37" if reste == 0 else "#E74C3C" # Or si payé, Rouge si reste
            st.markdown(f"""
            <div class='card'>
                <h4 style='margin:0'>{v['nom_client']}</h4>
                <small>{v['prestation']} | {v['created_at'].split('T')[0]}</small><br><br>
                <b>{t['total']}</b> {v['prix']}€<br>
                <span style='color:{color}'><b>{t['remains']}</b> {reste}€</span>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.write("Aucune donnée disponible.")

