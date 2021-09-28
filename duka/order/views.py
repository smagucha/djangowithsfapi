from django.shortcuts import render, redirect
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart
from django.urls import reverse
from django.contrib.auth.decorators import login_required


@login_required(login_url='/accounts/login/')
def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            # clear the cart
            cart.clear()
      
            request.session['order_id'] = order.id
            # redirect for payment
            return redirect(reverse('process'))
    else:
        form = OrderCreateForm()
    context={
    	'cart': cart, 'form': form
    }
    return render(request,'order/create.html',context)



    