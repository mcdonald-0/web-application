from django.contrib import admin
from .models import UserDetail, WebDetail

# Register your models here.
admin.site.register(UserDetail)

# TODO: i would like to edit the models so that, the user username and password can be viewed
#   accessed from their profile in the admin panel. i.e i need to edit the WebDetails in the models
#   so it could be registered.
