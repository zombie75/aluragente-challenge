from utils.lector_pdf import leer_pdf
from agentes.agente import dividir_texto


ruta = "documentos/manual_empresa.pdf"


texto = leer_pdf(ruta)


partes = dividir_texto(texto)


print("Cantidad de partes creadas:")
print(len(partes))


print("\nPrimera parte del documento:")
print(partes[0])