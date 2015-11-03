from django.db import models

class Client(models.Model):
	name = models.CharField(max_length=150)
	phone = models.IntegerField(blank=True,null=True)
	adress = models.CharField(max_length=250)
	email = models.EmailField()
	date = models.DateTimeField(auto_now_add=True)
	
	def __str__(self):
		return self.name 

class Finance(models.Model):
	product_name = models.CharField(max_length=150)
	price = models.IntegerField(blank=True,null=True)
	
	def __str__(self):
		return self.product_name
