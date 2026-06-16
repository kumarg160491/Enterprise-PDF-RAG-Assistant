from langchain_ollama import ChatOllama

from langchain_core.messages import (
    HumanMessage,
    AIMessage
)
from config import Config


class RAG:


    def __init__(self, vectorstore):

        self.retriever = vectorstore.as_retriever(
            search_kwargs={
                "k": 5
            }
        )


        self.llm = ChatOllama(
            model=Config.LLM_MODEL,
            temperature=0
        )


        self.history = []



    def ask(self, question):

        # Retrieve documents
        docs = self.retriever.invoke(
            question
        )
        context = "\n\n".join(
            [
                doc.page_content
                for doc in docs
            ]
        )
        history = "\n".join(
            [
                msg.content
                for msg in self.history
            ]
        )


        # Simple prompt

        prompt = f"""
            You are an enterprise document assistant.

            Answer only using the context.

            Context:
            {context}


            Conversation history:
            {history}


            Question:
            {question}

            """

        response = self.llm.invoke(
            prompt
        )
        # save memory

        self.history.append(
            HumanMessage(
                content=question
            )
        )
        
        self.history.append(
            AIMessage(
                content=response.content
            )
        )

        sources = []

        for doc in docs:

            sources.append(
                {
                    "file": doc.metadata.get("source"),
                    "page": doc.metadata.get("page")
                }
            )


        return response.content, sources