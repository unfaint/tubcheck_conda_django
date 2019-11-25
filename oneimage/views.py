from django.shortcuts import render, redirect
from django.http import JsonResponse


def check_results(request):
    return JsonResponse({'results': '1.0'}, status=201)
