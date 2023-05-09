from PyPDF2 import PdfReader #Lector de PDF
from langchain.embeddings.openai import OpenAIEmbeddings #Embeddings de OpenAI
from langchain.text_splitter import CharacterTextSplitter #Separador de texto por caracteres
from langchain.vectorstores import ElasticVectorSearch, Pinecone, Weaviate, FAISS #Vectorizador de texto
from langchain.chains.question_answering import load_qa_chain #Cadena de preguntas y respuestas
from langchain.llms import OpenAI #Modelo de lenguaje
import os
from settings import *

# Importar los modulos necesarios para el procedimiento 

os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY
# Cargar el PDF a analizar
reader = PdfReader(r"C:\Users\sebas\Downloads\mente-chat-gpt\data\MRAE-v3.pdf")
embeddings = OpenAIEmbeddings()

raw_text = ""
for i, page in enumerate(reader.pages):
    text = page.extract_text()
    if text:
        raw_text += text

text_splitter = CharacterTextSplitter(
    separator="\n",
    chunk_size=1000,
    chunk_overlap=200,
    length_function=len
)

texts = text_splitter.split_text(raw_text)

#docseach = FAISS.from_texts(texts, embeddings)

#docseach.save_local(r"C:\Users\sebas\Downloads\mente-chat-gpt\embeddings_")
docseach = FAISS.from_texts(texts, embeddings)
chain = load_qa_chain(OpenAI(), chain_type="stuff")

def pregunta (query:str):
    docs = docseach.similarity_search(query)
    return chain.run (input_documents=docs, question=query)


while True:
    prompt = str(input("Tú: "))
    if prompt == "salir":
        exit()
    print("Asistente: " + str(pregunta(prompt)))

