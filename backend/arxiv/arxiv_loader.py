import arxiv
import time

def search_arxiv(query, max_results=3):
    client = arxiv.Client(
        page_size=max_results,
        delay_seconds=5,
        num_retries=2
    )
    
    search = arxiv.Search(
        query=query,
        max_results=max_results,
        sort_by=arxiv.SortCriterion.Relevance
    )
    
    papers=[]
    
    try:
        results = client.results(search)
        
        for result in results:
            papers.append({
                "title":result.title,
                "author": [author.name for author in result.authors],
                "summary": result.summary,
                "pdf_url": result.pdf_url,
                "arxiv_id": result.entry_id
            })
            time.sleep(1)
            
    except Exception as e:
        print(f"arxiv search failed: {e}")
        
    return papers
    