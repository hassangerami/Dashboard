from django import forms
from .models import CreateModel, TicketModel


class CreateForm(forms.ModelForm):
    class Meta:
        model = CreateModel
        fields = '__all__'



class TicketForm(forms.ModelForm):
    class Meta:
        model = TicketModel
        fields = '__all__'
