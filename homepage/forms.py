from django import forms
from .models import UploadProfilePicture


class ImageUpload(forms.ModelForm):

    class Meta:
        model = UploadProfilePicture
        fields = ['caption', 'image']
