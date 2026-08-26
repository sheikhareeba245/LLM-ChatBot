import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

# Store conversation History
conversation_history=[]
print("ChatBot started! If you want to close it Please write exit. Thankyou! \n")
while True:
    user_input = input("Your Answer: ")
    if user_input.lower() =="exit":
        print("ChatBot is shutting down! Goodbye")
        break

    #Add user message in the history
    conversation_history.append(
        types.Content(role="user",parts=[types.Part(text=user_input)])
    )
    try:
        response=client.models.generate_content(
            model="gemini-3.5-flash-lite",
            contents=conversation_history
        )
        chatbot_reply=response.text
        print(f"ChatBot: {chatbot_reply}\n")

        # Add Chatbot reply in history
        conversation_history.append(
            types.Content(role="model",parts=[types.Part(text=chatbot_reply)])
        )
    except Exception as e:
        print(f"Error: {e}\n")


