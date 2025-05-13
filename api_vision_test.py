import openai
import os
import base64
from dotenv import load_dotenv

# Cargar API Key
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("API Key no definida en .env")

client = openai.OpenAI(api_key=api_key)

# Ruta de la imagen de prueba
image_path = "Texto_I_de_Gil_1799.png"  # Cambia esto por el nombre de tu archivo real

# Codificar la imagen en base64
with open(image_path, "rb") as image_file:
    base64_image = base64.b64encode(image_file.read()).decode('utf-8')

# Llamada a la API de visión
response = client.chat.completions.create(
    model="gpt-4o",  # O usa "gpt-4-turbo" si no tienes acceso a GPT-4o
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "Transcribe todo el texto presente en esta imagen:"},
                {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{base64_image}"}}
            ]
        }
    ],
    max_tokens=1024
)

# Mostrar la transcripción recibida
print("\n📄 Transcripción de la Imagen:\n")
print(response.choices[0].message.content)

print("\n---\n📊 Uso de tokens en la llamada:")
print(response.usage)
