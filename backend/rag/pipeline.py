from backend.rag.llm import get_llm

def ask_paper(question, vectorstore, chat_history=None, selected_paper=None):
    
    if selected_paper is None:
    #retrieve relevant chunks
        results = vectorstore.similarity_search(
            question, k=3
        )
    else:
        results = vectorstore.similarity_search(question, k=3, filter={"source_file":selected_paper})
    #combine retrieved content
    context_parts = []
    
    for i,document in enumerate(results, start=1):
        page = document.metadata.get("page", None)
        source_file = document.metadata.get(
                "source_file", "Unknown"
        )
        if page is not None:
            page_number = page+1
        else:
            page_number = "Unknown"
            
        context_parts.append(
            f"[Source {i}]\n"
            f"File: {source_file}\n"
            f"Page: {page_number}\n"
            f"Content: \n{document.page_content}"
        )
        
    context = "\n\n".join(context_parts)
    
    if not results:
        return (
            "I could not find this information in the selected paper.",
            []
        )
    
    if chat_history is None:
        chat_history = []
    history_text = ""
    for user_message, assistant_message in chat_history:
        history_text += (
            f"User: {user_message}\n"
            f"PaperMind: {assistant_message}\n\n"
        )
        
    prompt = f"""
    You are PaperMind, an AI assistant for research papers.

Answer the user's question using ONLY the provided context.

Rules:
1. Do not use information outside the context.
2. If the answer is not present, say:
   "I could not find this information in the paper."
3. Give a clear and concise answer.
4. Do not invent facts.
    
    Context:
    {context}
    Question:
    {question}
    
    Answer:
    """
    
    llm = get_llm()
    response = llm.invoke(prompt)
    
        #create unique sources
    unique_sources = []
    
    for document in results:
        page = document.metadata.get("page", None)
        source_file = document.metadata.get(
            "source_file",
            "Unknown"
        )
        if page is not None:
            source = f"{source_file} - Page {page+1}"
        else:
            source = f"{source_file} - Page Unknown"
            
        if source not in unique_sources:
            unique_sources.append(source)
            
    return response.text , unique_sources
    