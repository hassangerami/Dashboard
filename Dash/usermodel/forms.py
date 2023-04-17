from django import forms
from .models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import ReadOnlyPasswordHashField


class UserCreationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'full_name']

    def clean_email(self):
        email = self.cleaned_data['email']
        user = User.objects.filter(email=email).exists()

        if user:
            raise ValidationError('this is email already exists')
        return email


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField(help_text="for changed from <a href=\"..password/\">here</a>")

    class Meta:
        model = User
        fields = ['email', 'full_name', 'password', 'is_active', 'is_admin']
