from django.shortcuts import render, redirect
from .models import XRayImage, Competitor


def start_page(request):
    return render(request, 'uvsai/start_page.html')


def enter(request):
    if request.method == 'POST':
        email = request.POST['id_input']
        saved_users = Competitor.objects.filter(email=email)
        if saved_users.count() == 0:
            new_user = Competitor()
            new_user.email = email
            new_user.save()
        return redirect('/uvsai/0')
    else:
        return redirect('/uvsai/')


def xray_image(request, image_id):
    xray = XRayImage.objects.first()
    image_file_name = xray.file

    context = {
        'image_file_name': image_file_name,
    }

    return render(request, 'uvsai/xray_image.html', context)
