from django.shortcuts import render, reverse
from .models import UserDetail, WebDetail
from .forms import CreateProfileForm, LoginForm
from django.shortcuts import redirect
from django.http import HttpResponse
from django.views import View

# TODO: i need to convert these views to class based views so i need to do some research about class based
#   views and i need to implement them here


def index(requests):
    context = {}
    return render(requests, 'signup/index.html', context)


def login(requests):
    form = LoginForm()
    if requests.method == 'POST':
        form = LoginForm(requests.POST)
        if form.is_valid():
            try:
                WebDetail.objects.get(**form.cleaned_data)
                return HttpResponse('<h1>You are logged on</h1>')
            except WebDetail.DoesNotExist:
                context = {
                    'login_error': 'Sorry, you do not have an account, try creating one!',
                }
                return render(requests, 'profile.html', context)
    context = dict(form=form)
    return render(requests, 'signup/login.html', context)


def create_profile(requests):
    form = CreateProfileForm()
    if requests.method == "POST":
        form = CreateProfileForm(requests.POST)
        if form.is_valid():
            UserDetail.objects.create(**form.cleaned_data)
            # This is the email verification code
            # inactive_user = send_verification_email(requests, form)
            # inactive_user.cleaned_data['email']
            user_data = form.cleaned_data
            global user
            user = user_data
            return redirect('signup:web_profile_create')
    context = dict(form=form)
    return render(requests, 'signup/profile.html', context)


# TODO: i need to confirm the email verification. because i tried it and it didn't go well so i need
#  to connect to the internet and check it

def create_web_profile(requests):
    form = LoginForm()
    if requests.method == "POST":
        form = LoginForm(requests.POST)
        if form.is_valid():
            WebDetail.objects.create(**form.cleaned_data)
            return redirect('signup:welcome_page')
    context = dict(form=form)
    return render(requests, 'signup/web_profile.html', context)


def redirect_page(requests):
    # first_name, last_name = user['first_name'], user['last_name']
    context = {
        # 'first_name': first_name,
        # 'last_name': last_name,
    }
    return render(requests, 'signup/redirect_page.html', context)


# TODO: I need to modify the app so that a user cannot access the previous signup data from the url
#   i also need each signup to carry a unique identification so it is easily identified and that would be
#   stored in the database for the user.

# TODO: I need to add some style and color to this app, so i can publish it on github.
