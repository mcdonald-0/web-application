from django.db import models
# from login.signup.models import UserDetail


class UploadProfilePicture(models.Model):
    caption = models.CharField(max_length=2000)
    image = models.ImageField(upload_to='images/')

# max length for facebook caption is 63000 characters, instagram 2200, twitter 280, snapchat 32


class Profile(models.Model):
    # user = models.ForeignKey(UserDetail, on_delete=models.CASCADE)
    pass

# TODO: i need to google search how to add images in our model and then i need to do that for videos too.

# TODO: i need to install Pillow so i can work with image upload.
