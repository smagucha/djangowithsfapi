from django.db import models

# Create your models here.
class Catergory(models.Model):
	name= models.CharField(max_length = 50, unique= True)

	def __str__(self):
		return self.name

class Product(models.Model):
	name = models.CharField(max_length = 50, unique= True)
	price = models.FloatField()
	discount_price = models.FloatField(blank=True, null=True)
	category = models.ForeignKey(Catergory, on_delete = models.CASCADE)
	description = models.TextField()
	photo = models.ImageField(upload_to='images')

	def __str__(self):
		return self.name

