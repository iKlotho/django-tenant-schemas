from django import forms
from .models import Client
from django.forms import ModelForm


class ClientForm(ModelForm):

	class Meta:
		model = Client
		fields = ['name', 'description']

class GenerateUsersForm(forms.Form):
    pass
