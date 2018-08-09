from django.db import models

class MyCustomModel(models.Model):
	name = models.CharField(max_length=255, blank=True)
	name1 = models.CharField(max_length=255, blank=True)
	email = models.EmailField(null=True)