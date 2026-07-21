from utils.lector_pdf import leer_pdf


ruta = "documentos/Manual Interno de Empresa.pdf"

contenido = leer_pdf(ruta)

print(contenido)