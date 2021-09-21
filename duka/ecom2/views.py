from django.shortcuts import render

from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Catergory
import requests

# Create your views here.



def listproduct(request):
	list= Product.objects.all()
	context={
		'list': list
	}
	return render(request, 'ecom2/listproduct.html', context)


def category(request):
	cate = Catergory.objects.all()
	values=request.POST.get('q','')
	x = Catergory.objects.get(name=values)
	print(values)
	
	catefind= x.product_set.all()
	for i in catefind:
		print(i)
	context ={
		'cate': cate,
		'catefind': catefind,
	}

	return render(request, 'ecom2/catergory.html', context)