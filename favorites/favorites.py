from django.conf import settings
from shop.models import Product
from decimal import Decimal

class Favorites:
    def __init__(self, request):
        self.session = request.session
        favorites = self.session.get(settings.FAV_SESSION_ID)
        if not favorites:
            favorites = self.session[settings.FAV_SESSION_ID] = {}
        self.favorites = favorites

    def add(self, product: Product):
        product_id = str(product.id)
        if product_id not in self.favorites:
            self.favorites[product_id] = {'price': str(product.price)}
        else:
            del self.favorites[product_id]

        self.save()

    def __len__(self):
        return len(self.favorites)

    def save(self):
        self.session[settings.FAV_SESSION_ID] = self.favorites
        self.session.modified = True

    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.favorites:
            del self.favorites[product_id]
        self.save()

    def __iter__(self):
        product_ids = self.favorites.keys()
        products = Product.objects.filter(id__in=product_ids)
        products_map = {str(product.id): product for product in products}

        for product_id, item in self.favorites.items():
            product = products_map[product_id]

            item_copy = item.copy()
            item_copy['product'] = product
            item_copy['total_price'] = Decimal(item['price'])

            yield item_copy


    def clear(self):
        del self.session[settings.FAV_SESSION_ID]
        self.session.modified = True