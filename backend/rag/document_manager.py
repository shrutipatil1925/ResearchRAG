import os

PAPERS_DIR = "data/papers"

def get_available_papers():
    papers = []
    
    if not os.path.exists(PAPERS_DIR):
        return papers
    
    for filename in os.listdir(PAPERS_DIR):
        if filename.lower().endswith(".pdf"):
            papers.append(filename)
            
    return sorted(papers)

def select_paper(papers):
    print("\nSelect a paper:")
    print("0 - All papers")
    
    for index, paper in enumerate(papers, start=1):
        print(f"{index} - {paper}")
        
    while True:
        choice = input("\nEnter paper number : ")
            
        if choice == "0":
            return None 
            
        if choice.isdigit():
            index = int(choice)
                
            if 1 <= index <= len(papers):
                return papers[index-1]
                
        print("Invalid choice. Please try again.")