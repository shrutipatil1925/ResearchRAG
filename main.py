from backend.rag.loader import load_pdf
from backend.rag.chunker import split_documents
from backend.rag.embeddings import get_embedding_model
from backend.rag.vectorstore import (create_vectorstore, save_vectorstore, load_vectorstore)
from backend.rag.pipeline import ask_paper
from backend.rag.session_manager import load_session_history, save_session_history,get_chat_sessions, create_chat_session
from backend.multimodal.image_documents import load_image_descriptions
from backend.rag.document_manager import (get_available_papers, select_paper)
import os 

PAPERS_DIR = "data/papers"
VECTORSTORE_PATH = "data/vectorstore"
FAISS_INDEX_PATH = os.path.join(VECTORSTORE_PATH, "index.faiss")

print("Loading embedding model...")
embeddings = get_embedding_model()

print("\nAvailable Papers:")

papers = get_available_papers()

for paper in papers:
    print(f"- {paper}")
    
selected_paper = select_paper(papers)

if selected_paper is None:
    print("\nSelected: All papers")
else:
    print(f"\nSelected: {selected_paper}")

#check if FAISS already exists

if os.path.exists(FAISS_INDEX_PATH):
    print("\nExisting FAISS index found.")
    vectorstore = load_vectorstore(embeddings)

else:
    print("\nNo FAISS index found.")
    print("Processing PDF...")
    
    all_documents = []
    for file_name in os.listdir(PAPERS_DIR):
        if file_name.lower().endswith(".pdf"):
            file_path = os.path.join(PAPERS_DIR, file_name)
            print(f"Processing : {file_name}")
            documents = load_pdf(file_path)
            all_documents.extend(documents)
    
    print("\nLoading image descriptions...")
    image_documents = load_image_descriptions()
    all_documents.extend(image_documents)
    
    chunks = split_documents(all_documents)
    vectorstore = create_vectorstore(chunks, embeddings)
    save_vectorstore(vectorstore) 

print("\nAvailable Chat Sessions:")

sessions = get_chat_sessions()

if sessions:
    for index, session in enumerate(sessions, start=1):
        print(f"{index} - {session}")
else:
    print("No existing chat sessions.")

print("0 - Create new chat")

while True:

    choice = input("\nEnter chat number: ")

    if choice == "0":

        session_name = input(
            "Enter new chat name: "
        ).strip()

        if session_name:
            create_chat_session(session_name)
            break

        print("Chat name cannot be empty.")

    elif choice.isdigit():

        index = int(choice)

        if 1 <= index <= len(sessions):

            session_name = sessions[index - 1]
            break

        print("Invalid choice.")

    else:

        print("Invalid choice.")

chat_history = load_session_history(
    session_name
)

print("\nSelected Chat Session:")
print(session_name)    
    
while True:
    question = input(
        "\nAsk a question abount the paper"
        "(type 'exist' to quit):"
    )
    
    if question.lower() == "exit":
        break
    answer, sources = ask_paper(question, vectorstore,chat_history, selected_paper)
    chat_history.append((question, answer))
    save_session_history(session_name,chat_history)
    
    print("\nPaperMind:")
    print(answer)
    
    print("\nSources:")
    for source in sources:
        print(f"-{source}")