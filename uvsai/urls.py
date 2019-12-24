from django.urls import path
from .views import start_page, enter, ImageListView

urlpatterns = [
    path('', start_page),
    path('enter', enter),
    path('<int:id>', ImageListView.as_view())
]