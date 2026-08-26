import os
import json
from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

text = """
Ali is graduate now. He knows Java, python, data analysis,
and is currently learning about machine learning and APIs basics. Ali is 23 year old
and lives in Pakistan.
"""

prompt = f"""
Extract the name and skills from this text and return ONLY valid JSON,
no extra text, in this exact format:
{{"name": "...", "skills": ["...", "..."],"Location";".....","Age":"..."}}

Text: {text}
"""

try:
    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=prompt
    )

    raw_output = response.text
    print("ChatBot response: ")
    print(raw_output)

    cleaned = raw_output.strip().replace("```json", "").replace("```", "").strip()

    data = json.loads(cleaned)

    print("\nParsed Data: ")
    print("Name: ", data["name"])
    print("Skills: ", data["skills"])
    print("Age: ",data["Age"])
    print("Location: ",data["Location"])

except Exception as e:
    print(f"Error: {e}")
