from django.http import JsonResponse
from django.shortcuts import render
from PIL import Image
from tubcheck import ml_model
import os


def home_page(request):
    return render(request, 'oneimage/home.html')


def check_results(request):
    f = request.FILES['image']
    with open('tmp/image.jpg', 'wb+') as fp:
        for chunk in f.chunks():
            fp.write(chunk)
    with open('tmp/image.jpg', 'rb') as fp:
        image = Image.open(fp)
        output = ml_model(image)
    os.remove('tmp/image.jpg')
    return JsonResponse({'results': output['results']}, status=201)

