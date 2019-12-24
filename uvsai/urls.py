from django.urls import path
from .views import start_page, enter, xray_image

urlpatterns = [
    path('', start_page),
    path('enter', enter),
    path('<int:image_id>', xray_image)
]
