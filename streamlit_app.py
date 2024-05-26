import streamlit as st
import requests

API_URL = "https://tomas3254-legalbot.hf.space/api/v1/prediction/b21709c5-f495-4db2-9ca5-9f6129441557"

def query(payload):
    response = requests.post(API_URL, json=payload)
    return response.json()

st.title("Asistente de IA-Régimen de Riesgos del Trabajo (RRT)")

question = st.text_input("Pregunta:", "¡Hola! ¿En que puedo ayudarte?")
if st.button("Enviar"):
    with st.spinner("Consultando al modelo de IA..."):
        output = query({"question": question})
        st.write("Respuesta:")
        st.write(output)
