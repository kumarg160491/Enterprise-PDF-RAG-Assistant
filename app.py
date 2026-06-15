import streamlit as st
from config import config
from ingestion.loader import load_pdf_documents
from ingestion.splitter import split_documents
from ingestion.embeddings import get_embeddings
from vectorstore.store import create_vector_store
from rag.pipeline import RAG


st.title(
    "Enterprise PDF RAG Assistant"
)

@st.cache_resource
def load_app():

    docs=load_pdf_documents(
        config.DATA_PATH
    )
    chunks=split_documents(
        docs
    )
    embeddings=get_embeddings()
    db=create_vector_store(
        chunks,
        embeddings
    )
    return RAG(db)



rag=load_app()
question=st.chat_input(
    "Ask about documents..."
)

if question:
    answer,sources=rag.ask(
        question
    )
    with st.chat_message(
        "assistant"
    ):
        st.write(
            answer
        )
