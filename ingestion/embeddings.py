from langchain_ollama import OllamaEmbeddings
from config import Config

def get_embeddings():
    return OllamaEmbeddings(model=Config.EMBEDDING_MODEL)