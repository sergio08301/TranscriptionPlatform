import openai
import os
import base64
from django.conf import settings
import time

def transcribe_image_with_openai(image_path,max_attempts=4):
    client = openai.OpenAI(api_key=settings.OPENAI_API_KEY)

    with open(image_path, "rb") as image_file:
        base64_image = base64.b64encode(image_file.read()).decode('utf-8')

    prompt_message = "Extrae únicamente todo el texto legible de la imagen sin omitir nada. No expliques, solo devuelve el texto:"

    for attempt in range(1, max_attempts + 1):
        try:
            response = client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {
                        "role": "user",
                        "content": [
                            {"type": "text", "text": prompt_message},
                            {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{base64_image}"}}
                        ]
                    }
                ],
                max_tokens=1024
            )

            result = response.choices[0].message.content.strip()

            # Verificamos si la respuesta no es la negativa de la API
            if result != "I'm sorry, but I can't transcribe the content of this image.":
                return result

            print(f"Intento {attempt}: No se pudo transcribir, reintentando...")

            # Opcional: pausa entre intentos para evitar bloqueos
            time.sleep(1)

        except Exception as e:
            print(f"Error en el intento {attempt}: {e}")
            time.sleep(1)

        # Si tras los intentos sigue sin éxito
    return "I'm sorry, but I can't transcribe the content of this image."
