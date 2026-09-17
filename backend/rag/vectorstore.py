from langchain_community.vectorstores import FAISS
import os

VECTORSTORE_PATH = "data/vectorstore"

def create_vectorstore(chunks, embeddings):
    vectorstore = FAISS.from_documents(
        documents=chunks,
        embedding=embeddings
    )
    
    return vectorstore

def save_vectorstore(vectorstore):
    os.makedirs(VECTORSTORE_PATH, exist_ok=True)
    vectorstore.save_local(VECTORSTORE_PATH)
    print("FAISS vector store saved successfully!")
    
def load_vectorstore(embeddings):
    vectorstore = FAISS.load_local(
        VECTORSTORE_PATH, embeddings, allow_dangerous_deserialization=True
    )
    
    print('FAISS vector store loaded successfully!')
    
    return vectorstore