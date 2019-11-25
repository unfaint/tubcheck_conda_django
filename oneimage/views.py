from django.http import JsonResponse, HttpResponseRedirect
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import UploadFileForm
from PIL import Image
from io import BytesIO
from tubcheck import ml_model


def home_page(request):
    return render(request, 'oneimage/home.html')


def check_results(request):
    f = request.FILES['image']
    with open('tmp/image.jpg', 'wb+') as fp:
        for chunk in f.chunks():
            fp.write(chunk)
    with open('tmp/image.jpg', 'rb') as fp:
        image = Image.open(fp)
        output = ml_model(image)
    return JsonResponse({'results': output['results']}, status=201)


def upload_file(request):

    def handle_uploaded_file(f):
        with open('tmp/image.jpg', 'wb+') as fp:
            for chunk in f.chunks():
                fp.write(chunk)
        with open('tmp/image.jpg', 'rb') as fp:
            image = Image.open(fp)
            output_ = ml_model(image)
        return output_

    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            output = handle_uploaded_file(request.FILES['image'])
            print(output)
            return HttpResponseRedirect('/oneimage/')
    else:
        form = UploadFileForm()
    return render(request, 'oneimage/upload.html', {'form': form})
