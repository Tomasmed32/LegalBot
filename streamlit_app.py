import streamlit as st
import requests

API_URL = "https://tomas3254-legalbot.hf.space/api/v1/prediction/b21709c5-f495-4db2-9ca5-9f6129441557"

def query(payload):
    response = requests.post(API_URL, json=payload)
    return response.json()

st.title("Asistente de IA-Régimen de Riesgos del Trabajo (RRT)")

# Crear un formulario para la entrada de la pregunta
with st.form(key='query_form'):
    question = st.text_input("Pregunta:", "", placeholder="¡Hola! ¿En que puedo ayudarte?")
    submit_button = st.form_submit_button(label='Enviar')

# Verificar si el formulario ha sido enviado
if submit_button:
    with st.spinner("Consultando el modelo..."):
        output = query({"question": question})
        # Asegurarse de que el campo 'text' esté presente en la respuesta
        response_text = output.get('text', 'No se encontró el campo "text" en la respuesta.')
        st.write("Respuesta de la API:")
        # Mostrar la respuesta en un cuadro
        st.text_area("Respuesta", value=response_text, height=200)
