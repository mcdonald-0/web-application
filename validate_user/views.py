from django.shortcuts import render, render, redirect
from django.contrib.auth import login
from django.urls import reverse
from usersignup.forms import CreateProfileForm


# Create your views here.
def dashboard(requests):
    return render(requests, "users/dashboard.html")


def register(requests):
    context = {'form': CreateProfileForm}
    if requests.method == 'GET':
        return render(requests, 'users/register.html', context)

    elif requests.method == 'POST':
        form = CreateProfileForm(requests.POST)
        if form.is_valid():
            user = form.save()
            login(requests, user)
            return redirect(reverse('dashboard'))
