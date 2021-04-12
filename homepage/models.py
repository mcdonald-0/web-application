from django.db import models


class Upload(models.Model):
    text = models.CharField(max_length=1000)
    # image = models.ImageField()
