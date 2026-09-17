import requests
import os

def download_arxiv_paper(arxiv_id, output_dir="data/papers"):
    os.makedirs(output_dir, exist_ok=True)
    url = f"https://arxiv.org/pdf/{arxiv_id}"
    output_path = os.path.join(
        output_dir,
        f"arxiv_{arxiv_id}.pdf"
    )
    
    response = requests.get(url,timeout=30)
    
    response.raise_for_status()

    with open(output_path, "wb") as file:
        file.write(response.content)

    print(f"Paper downloaded successfully!")
    print(f"Saved to: {output_path}")

    return output_path