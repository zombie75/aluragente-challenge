from langchain_text_splitters import RecursiveCharacterTextSplitter


def dividir_texto(texto):

    separador = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    partes = separador.split_text(texto)

    return partes