from fastapi import FastAPI
from pydantic import BaseModel

from backend.rag.embeddings import get_embedding_model
from backend.rag.vectorstore import load_vectorstore
from backend.rag.pipeline import ask_paper

app = FastAPI(title="PaperMind API")

#Load embeddings and FAISS once when the API starts
print("Loading embedding model...")
embeddings = get_embedding_model()

print("Loading FAISS vector store...")
load_vectorstore = load_vectorstore(embeddings)

print("PaperMind backend ready!")

class ChatRequest(BaseModel):
    question: str
    selected_paper: str | None = None
    chat_history: list = []
    
@app.get("/")
def home():
    return {
        "message": "PaperMind API is running!"
    }
    
@app.post("/api/chat")
def chat(request: ChatRequest):
    answer, sources = ask_paper(
        question=request.question,
        vectorstore=load_vectorstore,
        chat_history=request.chat_history,
        selected_paper=request.selected_paper
    )
    
    return {
        "answer":answer,
        "sources":sources
    }