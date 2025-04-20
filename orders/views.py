from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from cart.cart import Cart
from .models import Order, OrderItem
from .forms import OrderCreateForm

def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                        product=item['product'],
                                        price=item['price'],
                                        quantity=item['quantity'])
            cart.clear()
            request.session['order_id'] = order.id
            return redirect(reverse('payment:process'))

    else:
        form = OrderCreateForm()

    return render(request, 'order/create.html', {'cart': cart, 'form': form})