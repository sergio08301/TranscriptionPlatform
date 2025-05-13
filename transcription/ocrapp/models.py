from django.db import models
from django.contrib.auth.models import User

class ImageUpload(models.Model):
    image = models.ImageField(upload_to='uploads/')
    transcription = models.TextField(blank=True)  # Añadimos el campo
    upload_time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"Imagen {self.id} subida por {self.user} el {self.upload_time}"
