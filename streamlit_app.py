import streamlit as st
from utils.lector_pdf import leer_pdf
from agentes.agente import dividir_texto, crear_memoria
from agentes.respuesta_ia import generar_respuesta

st.set_page_config(
    page_title="Gazzapo Assistant",
    page_icon="🤖"
)

st.title("🤖 Gazzapo Assistant")
st.write("Asistente inteligente para consultar informacion sobre productos "
         "personalizados, pedidos, envios, cambios, devoluciones y politicas de Gazzapo.")

# Cargar el documento
ruta = "documentos/manual_gazzapo_challenge.pdf"


@st.cache_resource
def cargar_memoria(ruta_pdf):
    texto = leer_pdf(ruta_pdf)
    partes = dividir_texto(texto)
    return crear_memoria(partes)


memoria = cargar_memoria(ruta)
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
