import os
from dotenv import load_dotenv
from google import genai
# load API key from .enc file
load_dotenv()
api_key= os.getenv("GEMINI_API_KEY")
# Make Client
client = genai.Client(api_key=api_key)
#Hardcoded prompt
prompt="Explain what an API is in simple words."
response=client.models.generate_content(
    model="gemini-2.5-flash-lite",
    contents=prompt
)

print(response.text)

