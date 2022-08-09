from django.db import models

# Create your models here.
class Contact(models.Model):
	Name=models.CharField(max_length=100)
	Phone=models.IntegerField()
	Email=models.EmailField(max_length=100)
	Message=models.CharField(max_length=500)