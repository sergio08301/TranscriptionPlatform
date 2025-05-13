from django.apps import AppConfig

class OcrappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ocrapp'

    def ready(self):
        import ocrapp.signals
