from backend.multimodal.image_documents import load_image_descriptions


documents = load_image_descriptions()

print("\nNumber of image documents:", len(documents))

for document in documents:

    print("\n" + "=" * 60)
    print("Source:", document.metadata["source_file"])
    print("Page:", document.metadata["page"] + 1)
    print("Type:", document.metadata["content_type"])
    print("Description:")
    print(document.page_content[:500])