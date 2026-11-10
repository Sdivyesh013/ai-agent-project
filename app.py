import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
print("Key loaded:", os.environ.get("GROQ_API_KEY")[:8] if os.environ.get("GROQ_API_KEY") else "NOT FOUND")

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

response = client.chat.completions.create(
    model="openai/gpt-oss-20b",
    messages=[
        {"role": "user", "content": "Say hello and tell me one fun fact about containers in computing."}
    ]
)

print(response.choices[0].message.content)