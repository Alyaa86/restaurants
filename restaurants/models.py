from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Restaurant(models.Model):
	name = models.CharField(max_length=200)
	description = models.TextField(max_length=500)
	image = models.ImageField(null=True, blank=True)
	opening_time = models.TimeField()
	closing_time = models.TimeField()
	owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

	def __str__(self):
		return self.name

class Item(models.Model):
	restaurant = models.ForeignKey(Restaurant, default=1, on_delete=models.CASCADE)
	name = models.CharField(max_length=200)
	description =models.TextField()
	price = models.DecimalField(max_digits=10, decimal_places=3)

	def __str__(self):
		return self.name

class Favourite(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
	