from langchain_ollama import ChatOllama

modelo = ChatOllama(
    model="gemma3:1b",
    temperature=0
)

def generar_respuesta(pregunta, contexto):

    prompt = f"""
Eres un asistente que responde preguntas sobre un documento interno de una empresa.

Este es el contenido del documento:

{contexto}

Pregunta del usuario:
{pregunta}

Responde únicamente utilizando la información del documento.
Si encuentras la respuesta, respóndela de forma clara.
Si realmente no aparece, responde:
"No encontré esa información en el documento."
"""

    respuesta = modelo.invoke(prompt)

    return respuesta.content