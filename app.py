from utils.lector_pdf import leer_pdf
from agentes.agente import dividir_texto, crear_memoria
from agentes.respuesta_ia import generar_respuesta


ruta = "documentos/manual_empresa.pdf"


texto = leer_pdf(ruta)

partes = dividir_texto(texto)

memoria = crear_memoria(partes)


pregunta = "¿Qué tecnologías utiliza la empresa?"


resultados = memoria.similarity_search(
    pregunta,
    k=3
    )


contexto = "\n".join(
    [documento.page_content for documento in resultados]
)


respuesta = generar_respuesta(
    pregunta,
    contexto
)


print(respuesta)