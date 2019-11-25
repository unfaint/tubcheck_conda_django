from django.urls import path
from .views import home_page, check_results, upload_file

urlpatterns = [
    path('', home_page),
    path('check', check_results),
    path('upload', upload_file),
]
