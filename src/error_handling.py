import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
load_dotenv()
print("======Test the wrong API Key======")
try:
    fake_client = genai.Client(api_key="hjkmj87965xsyv9u8")
    response=fake_client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents="Hello"
    )
    print(response.text)
except Exception as e:
    print(f"Error identified (Not Crashed): {e}\n")

print("===== Test 2: Timeout =====")
try:
    real_client=genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
    response=real_client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents="Hey! How are you?",
        config=types.GenerateContentConfig(
            http_options=types.HttpOptions(timeout=1)
        )
    )
    print(response.text)
except Exception as e:
    print(f"Timeout error identified: {e}\n")
print("Script Runs Successfully! Without Code Crashed" )
