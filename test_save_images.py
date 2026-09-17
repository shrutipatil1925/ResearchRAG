import os
from backend.multimodal.image_analyzer import analyze_image

IMAGE_DIR = "data/images"
OUTPUT_DIR = "data/image_descriptions"

os.makedirs(OUTPUT_DIR, exist_ok=True)

for filename in os.listdir(IMAGE_DIR):
    if not filename.lower().endswith(
        (".png",".jpg",".jpeg")
    ):
        continue
    
    image_path = os.path.join(IMAGE_DIR, filename)
    print(f"\nAnalyzing: {filename}")
    description = analyze_image(image_path)
    output_filename = os.path.splitext(filename)[0] + ".txt"
    output_path = os.path.join(OUTPUT_DIR,output_filename)
    with open(output_path,"w",encoding="utf-8") as file:
        file.write(description)
    print(f"Saved: {output_path}")
    
print("\nAll image descriptions saved successfully!")