# dharm# To run this code you need to install the following dependencies:
# pip install google-genai

import base64
import os
#File: /mount/src/dharm/app.py
#File "/mount/src/dharm/app.py"

#File "/mount/src/dharm/app.py"


def generate():
    
        api_key=os.environ.get("AIzaSyCQYZDUws4GzHOqop6-FC7UlMS4jXc3P-U"),
    )

    model = "gemini-2.5-pro"
    contents = [
        types.Content(
            "role", "user",
            parts=[
                types.Part.from_text(text="""INSERT_INPUT_HERE"""),
            ],
        ),
    ]
    generate_content_config = types.GenerateContentConfig(
        thinking_config = types.ThinkingConfig(
            thinking_budget=-1,
        ),
        response_mime_type="text/plain",
    )

    for chunk in client.models.generate_content_stream(
        model=model,
        contents=contents,
        config=generate_content_config,
    ):
        print(chunk.text, end="")

if __name__ == "__main__":
    
