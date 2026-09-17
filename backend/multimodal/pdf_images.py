import fitz
import os

def extract_images_from_pdf(pdf_path, output_dir="data/images"):
    os.makedirs(output_dir, exist_ok=True)
    pdf = fitz.open(pdf_path)
    extracted_images = []
    for page_number, page in enumerate(pdf):
        images = page.get_images(full=True)
        for image_number, image in enumerate(images):
            xref = image[0]
            image_data = pdf.extract_image(xref)
            image_bytes = image_data["image"]
            extension = image_data["ext"]
            
            filename = (
                f"page_{page_number + 1}"
                f"_image_{image_number + 1}"
                f".{extension}"
            )
            
            output_path = os.path.join(output_dir, filename)
            
            with open(output_path, "wb") as file:
                file.write(image_bytes)
                extracted_images.append(output_path)
                
    pdf.close()
    print(f"Extracted {len(extracted_images)} images")
    
    return extracted_images