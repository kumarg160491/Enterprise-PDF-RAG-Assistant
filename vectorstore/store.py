import os
from langchain_community.vectorstores import FAISS

def create_vector_store(documents, embeddings):
    db = FAISS.from_documents(documents, embeddings)
    return db

def save_vector_store(db, path):
    os.makedirs(path, exist_ok=True)
    db.save_local(path)

def load_vector_store(path, embeddings):
    return FAISS.load_local(path, embeddings, allow_dangerous_deserialization=True)