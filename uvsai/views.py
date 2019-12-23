from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from .models import XRayImage


def start_page(request):
    return render(request, 'uvsai/start_page.html')


def enter(request):
    if request.method == 'POST':
        return redirect('/uvsai/0')
    else:
        return redirect('/uvsai/')


class ImageListView(ListView):

    model = XRayImage
    paginate_by = 1

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context