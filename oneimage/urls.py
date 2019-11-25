from django.urls import path
from .views import check_redirect, check_results

urlpatterns = [
    path('check', check_redirect),
    path('results', check_results),
]
