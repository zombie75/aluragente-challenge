from utils.lector_pdf import leer_pdf


ruta = "documentos/manual_empresa.pdf"

contenido = leer_pdf(ruta)

print(contenido)