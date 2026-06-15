Architecture:

                 PDF Files
                    |
                    v
             PDF Loader
                    |
                    v
          Text Chunking
                    |
                    v
             Embeddings
                    |
                    v
              FAISS DB
                    |
                    v
              Retriever
                    |
                    v
        Conversation Memory
                    |
                    v
              Prompt
                    |
                    v
          Ollama LLM
                    |
                    v
            Streamlit UI



Folder Structure:

enterprise_pdf_rag/

│
├── app.py
├── config.py
├── requirements.txt
│
├── data/
│   └── documents/
│       ├── policy.pdf
│       └── manual.pdf
│
├── ingestion/
│   ├── loader.py
│   ├── splitter.py
│   └── embeddings.py
│
├── vectorstore/
│   └── store.py
│
├── rag/
│   └── pipeline.py
│
└── utils/
    └── logger.py# Enterprise-PDF-RAG-Assistant
