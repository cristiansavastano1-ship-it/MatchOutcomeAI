import streamlit as st
import pandas as pd

st.set_page_config(page_title="MatchOutcomeAI - Premier League", page_icon="⚽", layout="wide")

st.title("⚽ MatchOutcomeAI - Predizioni Premier League")
st.markdown("Questa applicazione web utilizza il machine learning per prevedere i risultati delle partite di calcio.")

# Sidebar per la selezione
st.sidebar.header("Impostazioni")
model_type = st.sidebar.selectbox("Seleziona Modello", ["Gradient Boosting", "XGBoost", "Logistic Regression", "SVM"])

st.subheader("Simulatore Partita")
col1, col2 = st.sidebar.columns(2)

home_team = st.sidebar.selectbox("Squadra in Casa", ["Arsenal", "Aston Villa", "Chelsea", "Liverpool", "Manchester City", "Manchester United", "Tottenham"])
away_team = st.sidebar.selectbox("Squadra Ospite", ["Brighton", "Crystal Palace", "Everton", "Newcastle", "West Ham", "Wolverhampton"])

if st.sidebar.button("Calcola Previsione"):
    st.info(f"Elaborazione in corso per **{home_team} vs {away_team}** con il modello {model_type}...")
    
    # Risultati simulati (collegabili a predictor.py)
    h_prob, d_prob, a_prob = 48.5, 25.0, 26.5
    
    col_res1, col_res2, col_res3 = st.columns(3)
    col_res1.metric(label=f"Vittoria {home_team}", value=f"{h_prob}%")
    col_res2.metric(label="Pareggio", value=f"{d_prob}%")
    col_res3.metric(label=f"Vittoria {away_team}", value=f"{a_prob}%")
    
    chart_data = pd.DataFrame({
        'Esito': ['1 (Casa)', 'X (Pareggio)', '2 (Ospite)'],
        'Probabilità (%)': [h_prob, d_prob, a_prob]
    })
    st.bar_chart(chart_data, x='Esito', y='Probabilità (%)')
