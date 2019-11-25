from django.urls import path
from .views import home_page, check_results

urlpatterns = [
    path('', home_page),
    path('check', check_results),
]
