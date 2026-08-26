import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

prompt = "Write a paragraph story about a reader. Which explain a life of a reader."
temperatures = [0.0, 1.0, 2.0]

for temp in temperatures:
    print(f"\n---- Temperature: {temp} ----")
    try:
        response = client.models.generate_content(
            model="gemini-3.6-flash",
            contents=prompt,
            config=types.GenerateContentConfig(
                temperature=temp
            )
        )
        print(response.text)
    except Exception as e:
        print(f"Error aayi: {e}")

# Loop se bahar
print("\n--- Max Token Test (very low limit) ---")
try:
    response = client.models.generate_content(
        model="gemini-2.5-flash-lite",
        contents="Write a paragraph story about a reader.",
        config=types.GenerateContentConfig(
            max_output_tokens=50
        )
    )
    print(response.text)
    print("Finish reason:", response.candidates[0].finish_reason)
except Exception as e:
    print(f"Error: {e}")
