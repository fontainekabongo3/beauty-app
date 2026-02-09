import streamlit as st
import pandas as pd

# Configuration pour que l'app soit belle sur téléphone
st.set_page_config(page_title="BeautyBusiness Pro", page_icon="💅", layout="centered")

# --- TITRE ---
st.title("💅 BeautyBusiness Pro")
st.subheader("Gère ton salon du bout des doigts")

# --- CHOIX DU MÉTIER ---
metier = st.selectbox("Ton métier :", ["Tresseuse", "Ongles", "Coiffure", "Esthéticienne"])

# --- SECTION 1 : ENCAISSEMENT ---
st.divider()
st.header("💰 Nouvel Encaissement")
montant = st.number_input("Montant de la prestation (€)", min_value=0, step=5)
nom_client = st.text_input("Nom de la cliente", placeholder="Ex: Sarah")

if st.button("Valider la vente"):
    st.balloons()
    st.success(f"Vente de {montant}€ enregistrée pour {nom_client} !")

# --- SECTION 2 : STOCKS ---
st.divider()
st.header("📦 État des Stocks")

# On crée un stock de base si c'est la première fois
if 'mon_stock' not in st.session_state:
    st.session_state.mon_stock = {"Produit A": 10, "Produit B": 5}

for prod, qte in st.session_state.mon_stock.items():
    col1, col2 = st.columns([2, 1])
    col1.write(f"**{prod}** : {qte} restants")
    if col2.button(f"Utiliser 1", key=prod):
        st.session_state.mon_stock[prod] -= 1
        st.rerun()

# --- SECTION 3 : RAPPEL SMS ---
st.divider()
st.header("📲 Relances Clients")
if st.button("Envoyer un rappel SMS automatique"):
    st.toast("Le SMS de rappel a été envoyé à la cliente de demain !")
