import os
import base64

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage

load_dotenv()


def analyze_image(image_path):

    llm = ChatGoogleGenerativeAI(
        model="gemini-3.1-flash-lite",
        temperature=0.2,
        google_api_key=os.getenv("GOOGLE_API_KEY")
    )

    # Read image
    with open(image_path, "rb") as image_file:
        image_data = base64.b64encode(
            image_file.read()
        ).decode("utf-8")

    # Multimodal message
    message = HumanMessage(
        content=[
            {
                "type": "text",
                "text": """
Analyze this image from a research paper.

Describe:
1. What the image represents
2. Important information shown in it
3. Any diagram, chart, table, labels, or relationships
4. A short summary useful for answering questions about the paper

Do not invent information that is not visible in the image.
"""
            },
            {
                "type": "image_url",
                "image_url": {
                    "url": f"data:image/png;base64,{image_data}"
                }
            }
        ]
    )

    response = llm.invoke([message])

    return response.text