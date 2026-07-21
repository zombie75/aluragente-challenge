from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()


def generar_respuesta(pregunta, contexto):

    modelo = ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0
    )

    prompt = f"""
    Eres un asistente empresarial.

    Utiliza solamente esta información:

    {contexto}

    Pregunta:
    {pregunta}

    Responde de forma clara y breve.
    """

    respuesta = modelo.invoke(prompt)

    return respuesta.content