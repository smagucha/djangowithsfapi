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
	print()
	return render(request, 'ecom2/product_details.html',context)


# def ecome_home(request):
# 	if request.session.test_cookie_worked():
# 		request.session.delete_test_cookie()
# 	else:
# 		request.session.set_test_cookie()
# 		messages.error(request, 'please enable cookie')

# 	return render(request, 'ecom2/cookie.html')

# def save_session_data(request):
# 	request.session['user_id']=20
# 	request.session['team']='arsenal'
# 	return HttpResponse('session data saved')

# def access_session_data(request):
# 	response =''
# 	if request.session.get('user_id'):
# 		user_id=request.session.get('user_id')
# 		response +='use id: {0} <br>'.format(user_id)
# 	if request.session.get('team'):
# 		team=request.session.get('team')
# 		response +='team: {0} <br>'.format(team)
# 	if not response:
# 		return HttpResponse('no session data')
# 	else:
# 		return HttpResponse(response)

# def delete_session_data(request):
# 	try:
# 		del request.session['user_id']
# 		del request.session['team']
# 	except KeyError:
# 		pass

# 	return HttpResponse('session data cleared')




