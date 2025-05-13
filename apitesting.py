import openai
import os
from dotenv import load_dotenv

# Cargar la API Key
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("API Key no definida en .env")

client = openai.OpenAI(api_key=api_key)

# Hacer la llamada de prueba
response = client.chat.completions.create(
    model="gpt-4-turbo",
    messages=[
        {"role": "user", "content": "Dime un chiste muy corto, por favor."}
    ],
    max_tokens=50
)

print("\nRespuesta de la API:\n")
print(response.choices[0].message.content)

print("\n---\nUso de tokens en la llamada:")
print(response.usage)