from django.urls import path, include
from . import views
from .views import dashboard, register

appname = 'validate_users'
urlpatterns = [
    path("", dashboard, name="dashboard"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("register/", register, name="register"),

]
