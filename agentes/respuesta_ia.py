from langchain_ollama import ChatOllama

modelo = ChatOllama(
    model="gemma3:270m",
    temperature=0
)


def generar_respuesta(pregunta, contexto):

    prompt = f"""
Responde la pregunta usando exclusivamente el CONTEXTO.

CONTEXTO:
{contexto}

PREGUNTA:
{pregunta}

INSTRUCCIONES:
- Busca primero la información en el contexto.
- Si el contexto contiene información relacionada, responde directamente.
- No inventes información.
- Responde en español.
- Sé breve y claro.
- Solo responde "No encontré esa información en el documento."
  cuando el contexto realmente no contenga ninguna información relacionada.

RESPUESTA:
"""

    respuesta = modelo.invoke(prompt)

    return respuesta.content
