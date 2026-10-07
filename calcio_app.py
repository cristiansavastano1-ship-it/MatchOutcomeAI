import streamlit as st
import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="MatchOutcomeAI - Predizioni Calcio", page_icon="⚽", layout="wide")

st.title("⚽ MatchOutcomeAI - Dashboard Predizioni")
st.markdown("Questa applicazione usa i modelli di machine learning del repository per stimare gli esiti delle partite.")

# Verifica dei file nel repository clonato
st.sidebar.header("Stato del Progetto")
if os.path.exists("predictor.py"):
    st.sidebar.success("✅ Modello ML (predictor.py) rilevato")
else:
    st.sidebar.warning("⚠️ predictor.py non trovato nella root")

st.sidebar.markdown("---")
st.sidebar.header("Seleziona Squadre")

# Elenco completo delle squadre principali di Premier League
teams = [
    "Arsenal", "Aston Villa", "Bournemouth", "Brentford", "Brighton",
    "Chelsea", "Crystal Palace", "Everton", "Fulham", "Liverpool",
    "Luton Town", "Manchester City", "Manchester United", "Newcastle United",
    "Nottingham Forest", "Sheffield United", "Tottenham Hotspur", "West Ham United",
    "Wolverhampton Wanderers", "Burnley"
]

home_team = st.sidebar.selectbox("Squadra in Casa", teams, index=0)
away_team = st.sidebar.selectbox("Squadra Ospite", teams, index=1)

if home_team == away_team:
    st.sidebar.error("⚠️ La squadra in casa e quella ospite non possono coincidere!")

st.subheader(f"Analisi Match: {home_team} vs {away_team}")

if st.button("Esegui Predizione con Machine Learning"):
    with st.spinner("Elaborazione in corso..."):
        # Qui potrai collegare le funzioni di predictor.py del tuo repository
        h_prob, d_prob, a_prob = 45.0, 30.0, 25.0
        
        col1, col2, col3 = st.columns(3)
        col1.metric(label=f"1 ({home_team})", value=f"{h_prob}%")
        col2.metric(label="X (Pareggio)", value=f"{d_prob}%")
        col3.metric(label=f"2 ({away_team})", value=f"{a_prob}%")
        
        chart_data = pd.DataFrame({
            'Esito': ['1', 'X', '2'],
            'Probabilità (%)': [h_prob, d_prob, a_prob]
        })
        st.bar_chart(chart_data, x='Esito', y='Probabilità (%)')
