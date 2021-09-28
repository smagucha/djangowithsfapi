from django.shortcuts import render, redirect, get_object_or_404
from ecom2.models import Product
from .cart import Cart
from django.views.decorators.http import require_POST
from .forms import CartForm
from django.contrib.auth.decorators import login_required

@login_required(login_url='/accounts/login/')
def cart_add(request, product_id):
	cart = Cart(request)
	product = get_object_or_404(Product, id=product_id)
	form = CartForm(request.POST)
	if request.method =='POST':
		if form.is_valid():
			cd = form.cleaned_data
			cart.add(
				product=product,
				quantity=cd['quantity'],
				override_quantity=cd['override']
				)
	return redirect('cart_detail')
	
@login_required(login_url='/accounts/login/')
def cart_remove(request, product_id):
	cart = Cart(request)
	product = get_object_or_404(Product, id=product_id)
	cart.remove(product)
	return redirect('cart_detail')

@login_required(login_url='/accounts/login/')
def cart_detail(request):
	cart = Cart(request)
	for item in cart:
		item['update_quantity_form'] = CartForm(initial={
			'quantity': item['quantity'],
			'override': True
			})
	return render(request, 'cart/detail.html', {'cart': cart})
	
	


