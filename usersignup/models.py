from django.db import models


class WebDetail(models.Model):
    # user = models.OneToOneField(UserDetail, on_delete=models.CASCADE, primary_key=True,)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.username


class UserDetail(models.Model):
    first_name = models.CharField(max_length=225)
    middle_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    user = models.OneToOneField(WebDetail, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.first_name


