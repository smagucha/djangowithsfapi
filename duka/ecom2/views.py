from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Catergory
import requests
from cart.forms import CartForm
from django.contrib import messages

# Create your views here.

def listproduct(request):
	list= Product.objects.all()
	context={
		'list': list
	}
	return render(request, 'ecom2/listproduct.html', context)

def category(request):
	cate = Catergory.objects.all()
	catefind = None
	if request.method == 'POST':
		values=request.POST.get('q','')
		x = Catergory.objects.get(name=values)
		catefind= x.product_set.all()
	context ={
		'catefind': catefind,
		'cate': cate, 
	}
	return render(request, 'ecom2/catergory.html', context)


def product_detail(request, id):
	product = Product.objects.get(id =id)
	cart_product_form = CartForm()
	context ={
		'product': product,
		'cart_product_form': cart_product_form,
	}
	return render(request, 'ecom2/product_details.html',context)
