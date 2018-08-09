from django.forms import ModelForm
from .models import MyCustomModel

class CustomForm(ModelForm):

	class Meta:
		model = MyCustomModel
		fields = '__all__'