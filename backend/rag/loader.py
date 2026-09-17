from langchain_community.document_loaders import PyMuPDFLoader
import os

def load_pdf(file_path):
    loader = PyMuPDFLoader(file_path)
    documents = loader.load()
    file_name = os.path.basename(file_path)
     
    for document in documents:
        document.metadata["source_file"] = file_name
        
    print(f"Loaded {len(documents)} pages")
    
    return documents