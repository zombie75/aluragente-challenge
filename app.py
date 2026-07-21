from utils.lector_pdf import leer_pdf
from agentes.agente import dividir_texto, crear_memoria


ruta = "documentos/manual_empresa.pdf"


texto = leer_pdf(ruta)

partes = dividir_texto(texto)


memoria = crear_memoria(partes)


print("Memoria creada correctamente")


pregunta = "¿Qué tecnologías utiliza la empresa?"


resultado = memoria.similarity_search(pregunta)


print("\nResultado encontrado:")
print(resultado[0].page_content)