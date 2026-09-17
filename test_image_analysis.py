from backend.multimodal.image_analyzer import analyze_image

image_path = "data/images/page_2_image_1.png"
result = analyze_image(image_path)

print("\nImage Analysis : ")
print(result)