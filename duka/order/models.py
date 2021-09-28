from django.db import models
from ecom2.models import Product



class Order(models.Model):
	braintree_id = models.CharField(max_length=150, blank=True, null = True)
	first_name = models.CharField(max_length=50, blank=True, null = True)
	last_name = models.CharField(max_length=50,blank=True, null = True)
	email = models.EmailField(blank=True, null = True)
	address = models.CharField(max_length=250, blank=True, null = True)
	postal_code = models.CharField(max_length=20, blank=True, null = True)
	city = models.CharField(max_length=100,blank=True, null = True)
	created = models.DateTimeField(auto_now_add=True, blank=True, null = True)
	updated = models.DateTimeField(auto_now=True,blank=True, null = True)
	paid = models.BooleanField(default=False,blank=True, null = True)

	class Meta:
		ordering = ('-created',)
	def __str__(self):
		return f'Order {self.id}'
	def get_total_cost(self):
		return sum(item.get_cost() for item in self.items.all())
	
	class Meta:
		ordering = ('-created',)

	def __str__(self):
		return f'Order {self.id}'

	def get_total_cost(self):
		return sum(item.get_cost() for item in self.items.all())

class OrderItem(models.Model):
	order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
	product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
	price = models.DecimalField(max_digits=10, decimal_places=2)
	quantity = models.PositiveIntegerField(default=1)
	
	def __str__(self):
		return str(self.id)
	
	def get_cost(self):
		return self.price * self.quantity
