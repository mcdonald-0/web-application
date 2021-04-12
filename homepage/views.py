from django.shortcuts import render


def index(requests):
    context ={}
    return render(requests, 'homepage/index2.html', context)
