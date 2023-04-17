from django import forms
from usermodel.models import User
from django.core.exceptions import ValidationError



class SignUpForm(forms.Form):
    full_name = forms.CharField(max_length=255, label_suffix="")
    email = forms.EmailField(label_suffix="")
    password = forms.CharField(widget=forms.PasswordInput, label_suffix="")

    def __str__(self):
        return f'{self.full_name}'
    
    
    def clean_email(self):
        email = self.cleaned_data['email']
        user = User.objects.filter(email=email).exists()

        if user:
            raise ValidationError('This email is invalid')
        return email
    


class SignInForm(forms.Form):
    email = forms.EmailField(label_suffix="")
    password = forms.CharField(widget=forms.PasswordInput, label_suffix="")

    def __str__(self):
        return f'{self.email}'
    