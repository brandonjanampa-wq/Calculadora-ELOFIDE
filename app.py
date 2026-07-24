import streamlit as st

st.set_page_config(
    page_title="Calculadora Elo FIDE",
    page_icon="♟",
    layout="centered"
)

st.title("♟ Calculadora Elo FIDE")

st.write("Calcula cuánto Elo ganarás o perderás según la fórmula oficial de la FIDE.")

ELO_Actual = st.number_input(
    "Tu Elo",
    min_value=100.0,
    max_value=3500.0,
    value=1800.0,
    step=1.0
)

ELO_Rival = st.number_input(
    "Elo del rival",
    min_value=100.0,
    max_value=3500.0,
    value=1800.0,
    step=1.0
)

K = st.selectbox(
    "Factor K",
    [40, 20, 10]
)

resultado = st.selectbox(
    "Resultado",
    ["Victoria", "Tablas", "Derrota"]
)

if resultado == "Victoria":
    S = 1
elif resultado == "Tablas":
    S = 0.5
else:
    S = 0

if st.button("Calcular"):

    E = 1 / (1 + (10 ** ((ELO_Rival - ELO_Actual) / 400)))

    cambio = K * (S - E)

    ELO_Nuevo = ELO_Actual + cambio

    st.success(f"Ganancia/Pérdida de Elo: {cambio:+.2f}")

    st.info(f"Nuevo Elo: {ELO_Nuevo:.2f}")