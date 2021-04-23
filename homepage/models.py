from django.db import models
from usersignup.models import WebDetail


class Profile(models.Model):
    user = models.ForeignKey(WebDetail, on_delete=models.CASCADE)


class UploadProfilePicture(models.Model):
    # i need to install RichTextField so i would put it below
    caption = models.CharField(max_length=2000, blank=True, null=True)
    image = models.ImageField(upload_to='images/')
    # research on datefield, and related name argument
    date_uploaded = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(WebDetail, on_delete=models.CASCADE)






