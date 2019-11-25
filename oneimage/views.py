from django.shortcuts import render, redirect
from django.http import JsonResponse
from PIL import Image
from tubcheck import ml_model


def check_results(request):
    image = Image.frombytes(request.POST['image'])
    output = ml_model(image)
    return JsonResponse({'results': output['results']}, status=201)
