
from django.shortcuts import render, redirect
from .forms import ImageUploadForm
from .models import ImageUpload
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.urls import reverse
from django.utils.text import slugify
from .utils import transcribe_image_with_openai


def home(request):
    transcription_result = None
    image_url = None

    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            if request.user.is_authenticated:
                instance.user = request.user
            instance.save()

            try:
                instance.transcription = transcribe_image_with_openai(instance.image.path)
            except Exception as e:
                instance.transcription = f"❌ Error al procesar la imagen: {str(e)}"
            instance.save()

            # Redirigimos para evitar reenvío de formulario y mantener los datos
            return redirect(f"{reverse('home')}?image_id={instance.id}")
    else:
        form = ImageUploadForm()
        image_id = request.GET.get('image_id')
        if image_id:
            try:
                instance = ImageUpload.objects.get(id=image_id)
                transcription_result = instance.transcription
                image_url = instance.image.url
            except ImageUpload.DoesNotExist:
                pass

    return render(request, 'ocrapp/home.html', {
        'form': form,
        'transcription_result': transcription_result,
        'image_url': image_url
    })


def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            if request.user.is_authenticated:
                instance.user = request.user

            instance.save()
            # Llamar a la API de OpenAI para transcribir la imagen
            try:
                transcription = transcribe_image_with_openai(instance.image.path)
            except Exception as e:
                transcription = f"Error al procesar la imagen: {str(e)}"

            print(f"Ruta de la imagen: {instance.image.path}")

            # Placeholder en lugar de llamada a API (por si quiero hacer pruebas sin llamar a la api y gastar pasta)
            #instance.transcription = "Aquí irá la transcripción generada por IA."
            instance.transcription = transcription
            instance.save()

            return render(request, 'ocrapp/result.html', {'instance': instance})
    else:
        form = ImageUploadForm()
    return render(request, 'ocrapp/upload.html', {'form': form})


def history(request):
    if not request.user.is_authenticated:
        return render(request, 'ocrapp/history_guest.html')

    images_list = ImageUpload.objects.filter(user=request.user).order_by('-upload_time')
    paginator = Paginator(images_list, 5)  # 5 imágenes por página (puedes ajustar el número)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'ocrapp/history.html', {'page_obj': page_obj})

from django.shortcuts import get_object_or_404, redirect

@login_required
def delete_image(request, image_id):
    image = get_object_or_404(ImageUpload, id=image_id, user=request.user)
    image.delete()
    return redirect('history')

@login_required
def export_transcription(request,image_id):
    image= get_object_or_404(ImageUpload,id=image_id, user=request.user)

    filename = slugify(f"transcription_{image.upload_time}") + ".txt"
    response = HttpResponse(image.transcription, content_type='text/plain')
    response['Content-Disposition'] = f'attachment; filename="{filename}"'
    return response

def export_txt(request, image_id):
    image = get_object_or_404(ImageUpload, id=image_id, user=request.user)
    filename = slugify(f"transcription_{image.upload_time}") + ".txt"
    response = HttpResponse(image.transcription, content_type='text/plain')
    response['Content-Disposition'] = f'attachment; filename="{filename}"'
    return response