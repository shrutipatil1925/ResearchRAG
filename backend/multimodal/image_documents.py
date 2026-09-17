import os
from langchain_core.documents import Document

IMAGE_DESCRIPTION_DIR = "data/image_descriptions"

def load_image_descriptions():
    documents = []
    if not os.path.exists(IMAGE_DESCRIPTION_DIR):
        return documents
    
    for filename in os.listdir(IMAGE_DESCRIPTION_DIR):
        if not filename.endswith(".txt"):
            continue
        
        file_path = os.path.join(IMAGE_DESCRIPTION_DIR, filename)
        with open(file_path,"r", encoding="utf-8") as file:
            description = file.read()
            
            page_number = "Unknown"
            parts = filename.split("_")
            
            if len(parts)>=2:
                page_number = parts[1]
                
            document = Document(page_content=description,
                                metadata={
                                    "source_file":filename,
                                    "page": int(page_number)-1
                                    if page_number.isdigit()
                                    else None,
                                    "content_type":"image"
                                }
                            )
            documents.append(document)
            
        print(
            f"Loaded {len(documents)} image descriptions"
        )
        
        return documents