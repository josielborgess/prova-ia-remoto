import os
import streamlit as st
import requests

API_URL = os.getenv("API_URL", "http://localhost:8000")

st.set_page_config(page_title="Prova IA Generativa – Starter UI")

st.title("Hello, World! 👋")
st.write(
    "Esta é a interface inicial. "
    "Implemente aqui as funcionalidades conforme documentação."
)

if st.button("Testar conexão com backend"):
    try:
        r = requests.get(f"{API_URL}/health", timeout=5)
        if r.ok:
            st.success(f"Backend online: {r.json()}")
        else:
            st.error(f"Backend respondeu {r.status_code}: {r.text}")
    except requests.RequestException as e:
        st.error(f"Falha na requisição: {e}")
