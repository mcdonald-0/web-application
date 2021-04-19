from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *


def index(requests):
    context = {}
    return render(requests, 'homepage/index.html', context)


def image_view(requests):
    if requests.method == "POST":
        form = ImageUpload(requests.POST, requests.FILES)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = ImageUpload()
    return render(requests, 'homepage/image.html', {'form': form})


def success(requests):
    return HttpResponse('Image successfully uploaded')
