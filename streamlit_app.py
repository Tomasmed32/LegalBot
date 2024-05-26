import streamlit as st
import requests

API_URL = "https://tomas3254-legalbot.hf.space/api/v1/prediction/b21709c5-f495-4db2-9ca5-9f6129441557"

def query(payload):
    response = requests.post(API_URL, json=payload)
    return response.json()

st.title("Consulta a la API de Flowise")

question = st.text_input("Pregunta:", "Hey, how are you?")
if st.button("Enviar"):
    with st.spinner("Consultando la API..."):
        output = query({"question": question})
        st.write("Respuesta de la API:")
        st.write(output)
