from backend.rag.document_manager import get_available_papers


papers = get_available_papers()

print("\nAvailable Papers:")

for paper in papers:
    print("-", paper)