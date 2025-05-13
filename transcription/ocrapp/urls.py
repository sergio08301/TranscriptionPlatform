from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('subir/', views.upload_image, name='upload_image'),
    path('historial/', views.history, name='history'),
    path('eliminar/<int:image_id>/', views.delete_image, name='delete_image'),
    path('exportar/<int:image_id>/', views.export_transcription, name='export_transcription'),


]