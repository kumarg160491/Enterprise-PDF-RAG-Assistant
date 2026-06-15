from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader

def load_pdf_documents(path):
    documents = []

    for file in Path(path).glob("*.pdf"):
        loader = PyPDFLoader(str(file))
        docs = loader.load()
        documents.extend(docs)
    
    return documents