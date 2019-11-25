from django.urls import path
from .views import check_results

urlpatterns = [
    path('check', check_results),
]
