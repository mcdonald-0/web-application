from django.urls import path
from . import views

app_name = 'usersignup'
urlpatterns = [
    path('', views.index, name='homepage'),
    path('login/', views.login, name='login_page'),
    path('signup/', views.create_profile, name='create_profile'),
    path('signup/final', views.create_web_profile, name='web_profile_create'),
    path('welcome/', views.redirect_page, name='welcome_page')
]