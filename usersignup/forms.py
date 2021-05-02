import re
from .models import UserDetail
from django import forms
from django.core.validators import ValidationError


def has_only_english(word):
    all_alphabets = '[\u0041-\u007A\-]*'
    return bool(re.fullmatch(all_alphabets, word))


def has_symbols(word):
    symbols = '[\u005B-\u0060\-]*'
    return bool(re.fullmatch(symbols, word))


class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=95,
        min_length=6,
        label="",
        widget=forms.TextInput(
            attrs={'placeholder': 'Username'}
        )
    )
    password = forms.CharField(
        max_length=128,
        min_length=8,
        label="",
        widget=forms.PasswordInput(
            attrs={'placeholder': 'Password'}
        ),
    )


class CreateProfileForm(forms.Form):
    first_name = forms.CharField(
        max_length=26,
        min_length=2,
        label="",
        widget=forms.TextInput(
            attrs={'placeholder': 'First name'}
        )
    )
    middle_name = forms.CharField(
        max_length=26,
        min_length=2,
        label="",
        required=False,
        widget=forms.TextInput(
            attrs={'placeholder': 'Middle name'}
        )
    )
    last_name = forms.CharField(
        max_length=26,
        min_length=2,
        label="",
        widget=forms.TextInput(
            attrs={'placeholder': 'Last name'}
        )
    )
    email = forms.EmailField(
        max_length=254,
        min_length=10,
        label="",
        widget=forms.TextInput(
            attrs={'placeholder': 'Email'}
        ),
    )

    def clean_first_name(self):
        if has_only_english(self.cleaned_data['first_name']):
            return self.cleaned_data['first_name']
        error_message = 'This has to be plain english, e.g John'
        raise ValidationError(error_message, code='invalid_language')

    def clean_first_name_to_check_for_symbols(self):
        if has_only_english(self.cleaned_data['first_name']):
            return self.cleaned_data['first_name']
        error_message = 'Name cannot contain \' [, \, ], ^, -, ` \''
        raise ValidationError(error_message, code='symbol_included')

    def clean_middle_name(self):
        if has_only_english(self.cleaned_data['middle_name']):
            return self.cleaned_data['middle_name']
        error_message = 'This has to be plain english, e.g Maxwell'
        raise ValidationError(error_message, code='invalid_language2')

    def clean_last_name(self):
        if has_only_english(self.cleaned_data['last_name']):
            return self.cleaned_data['last_name']
        error_message = 'This has to be plain english, e.g Smith'
        raise ValidationError(error_message, code='invalid_language3')

    # def clean_email(self, *args, **kwargs):
    #     email = self.cleaned_data.get('email')
    #     if not email.endswith('.com'):
    #         raise forms.ValidationError(
    #             _('This is not a valid email'),
    #             code='Invalid'
    #         )
    #     return email


# TODO:
#  i need to adjust the redirect function so that a user would not just
#  in the url and then have access to the last user signup detail.
#   i also need to add a gender to the forms view

# TODO: I need to clean every data that comes in, and also google search the minimum and maximum length for
#  every field listed above.

'''
Unicode character for punctuations and symbols 0020-002F
Unicode character for digits 0030-0039
Unicode character for punctuations and symbols 003A-0040
Unicode character for english uppercase 0041-005A
Unicode character for punctuations and symbols 005B-0060
Unicode character for english lowercase 0061-007A
Unicode character for punctuations and symbols 007B-007E
'''
