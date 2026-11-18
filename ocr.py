from pathlib import Path
from ollama import Client

def ProcessImgage(path_to_image):
    client = Client(host="http://localhost:48564")
    image_path = Path(__file__).with_name(path_to_image)

    response = client.chat(
        model="glm-ocr",
        messages=[
            {
                "role": "user",
                "content": "Text Recognition",
                "images": [str(image_path)],
            }
        ],
    )
    #debug
    print(response.message.content)
    return response.message.content