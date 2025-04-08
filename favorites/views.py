from django.shortcuts import render, get_object_or_404
from .favorites import Favorites
from shop.models import Product
from django.http import JsonResponse
from django.views.decorators.http import require_POST


@require_POST
def favorites_add(request, product_id):
    favorites = Favorites(request)
    product = get_object_or_404(Product, id=product_id)
    favorites.add(product)

    return JsonResponse({
        'success': True,
        'total_items': len(favorites)
    })

@require_POST
def favorites_remove(request, product_id):
    favorites = Favorites(request)
    product = get_object_or_404(Product, id=product_id)
    favorites.remove(product)
    return JsonResponse({
        'success': True,
        'total_items': len(favorites)
    })


def favorites_detail(request):
    favorites = Favorites(request)
    return render(request,
                  'favorites/favorites_detail.html',
                  {'favorites': favorites})