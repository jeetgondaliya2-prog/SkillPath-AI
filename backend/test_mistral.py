import os
from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI

load_dotenv()

api_key = os.getenv("MISTRAL_API_KEY")

print("API KEY FOUND:", bool(api_key))

model = ChatMistralAI(
    model="mistral-small-latest",
    api_key=api_key
)

response = model.invoke("Say hello in one sentence.")

print(response.content)