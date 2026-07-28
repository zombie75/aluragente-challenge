from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings


def dividir_texto(texto):

    separador = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    partes = separador.split_text(texto)

    return partes


def crear_memoria(partes):

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    memoria = FAISS.from_texts(
        partes,
        embeddings
    )
    return memoria

