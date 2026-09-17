from backend.arxiv.arxiv_loader import search_arxiv

papers = search_arxiv("retrieval agumented generation", max_results=3)

for paper in papers:
    print("\nTitle:",paper["title"])
    print("Authors:",paper["authors"])
    print("PDF:",paper["pdf_url"])
    print("arxiv ID:", paper["arxiv_id"])