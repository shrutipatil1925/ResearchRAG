import os
from backend.multimodal.image_analyzer import analyze_image

IMAGE_DIR = "data/images"

for filename in os.listdir(IMAGE_DIR):
    if filename.lower().endswith((".png", ".jpg", ".jpeg")):
        image_path = os.path.join(IMAGE_DIR,filename)
        print("\n" + "=" * 60)
        print(f"Analyzing: {filename}")
        print("=" * 60)
        
        result = analyze_image(image_path)
        print(result)