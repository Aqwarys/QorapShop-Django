from django.shortcuts import redirect, get_object_or_404, render
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from shop.models import Product
from .cart import Cart

@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.add(product)
    return JsonResponse({'message': 'Товар добавлен', 'total_items': len(cart)})

def cart_update(request):
    """ Обновление количества товара в корзине через AJAX """
    if request.method == "POST":
        cart = Cart(request)
        product_id = request.POST.get("product_id")
        action = request.POST.get("action")
        product = get_object_or_404(Product, id=product_id)
        if action == "increase":
            cart.add(product=product, quantity=cart.cart[product_id]['quantity']+1, update_quantity=True)
        elif action == "decrease":
            if cart.cart[product_id]['quantity'] > 1:
                cart.add(product=product, quantity=-1, update_quantity=True)
            else:
                cart.remove(product)
        elif action == "remove":
            cart.remove(product)

        return JsonResponse({
            "success": True,
            "quantity": cart.cart[product_id]["quantity"] if product_id in cart.cart else 0,
            "total_price": cart.get_item_total_price(product) if product_id in cart.cart else 0,
            "cart_total": cart.get_total_price()
        })

    return JsonResponse({"success": False}, status=400)

def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart_detail')

def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart/cart_detail.html', {'cart': cart})
