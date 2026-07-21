import streamlit as st

from utils.lector_pdf import leer_pdf
from agentes.agente import dividir_texto, crear_memoria
from agentes.respuesta_ia import generar_respuesta

st.set_page_config(
    page_title="AluraAgente",
    page_icon="🤖"
)

st.title("🤖 AluraAgente")
st.write("Haz preguntas sobre el manual interno de la empresa.")

# Cargar el documento
ruta = "documentos/manual_empresa.pdf"

texto = leer_pdf(ruta)
partes = dividir_texto(texto)
memoria = crear_memoria(partes)

pregunta = st.text_input("Escribe tu pregunta:")

if st.button("Consultar"):

    if pregunta:

        resultados = memoria.similarity_search(
            pregunta,
            k=3
        )

        contexto = "\n".join(
            [doc.page_content for doc in resultados]
        )

        respuesta = generar_respuesta(
            pregunta,
            contexto
        )

        st.subheader("Respuesta")
        st.success(respuesta)

    else:
        st.warning("Escribe una pregunta.")