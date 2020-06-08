from django.shortcuts import render
from django.http import HttpResponse
from imageApp.forms import NameForm
from imageApp.models import Galary
from django.conf import settings
from PIL import Image, ImageOps


def full_image_path(request):
    image_path = '/'.join(request.path.split('/')[2:])
    expansion = request.path.split('/')[-1].split('.')[-1]
    full_image_path = f"{settings.MEDIA_ROOT}/{image_path}"
    return full_image_path, expansion

def image_resize(request, img):
    try:
        width = int(request.GET.get('width', None))
    except:
        width = None
    try:
        height = int(request.GET.get('height', None))
    except:
        height = None

    if width and height:
        size = width, height
        img = ImageOps.fit(img, size, Image.ANTIALIAS)

    elif width:
        size = width, img.height
        img = ImageOps.fit(img, size, Image.ANTIALIAS)

    elif height:
        size = img.width, height
        img = ImageOps.fit(img, size, Image.ANTIALIAS)
    return img


def quality_image(response,img,request):
    try:
        quality = int(request.GET.get('quality', None))
    except:
        quality = None

    if quality:
        img.save(response, 'JPEG', quality=quality)
    else:
        img.save(response, 'JPEG')

def gelaryApp(request):
    if request.method == 'POST' and request.FILES['image']:
        form = NameForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    form = NameForm()
    images = Galary.objects.all()
    return render(request, 'imageApp/imageApp.html', {'form':form, 'images':images})

def mediaApp(request):
    image_path, expansion = full_image_path(request=request)
    img = Image.open(image_path, mode='r')
    img = image_resize(request=request, img=img)
    response = HttpResponse(content_type=f'image/{expansion}')
    quality_image(response, img, request)
    return response