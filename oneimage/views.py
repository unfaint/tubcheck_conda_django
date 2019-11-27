from django.http import JsonResponse
from django.shortcuts import render
from PIL import Image
from tubcheck import ml_model
import os
import io


def home_page(request):
    return render(request, 'oneimage/home.html')


def check_results(request):
    f = request.FILES['image']
    b = io.BytesIO()
    for chunk in f.chunks():
        b.write(chunk)

    b.seek(0)
    image = Image.open(b)
    output = ml_model(image)
    return JsonResponse({'results': output['results']}, status=201)
