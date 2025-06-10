from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('shop.urls', namespace='shop')),
    path('cart/', include('cart.urls', namespace='cart')),
    path('favorites/', include('favorites.urls', namespace='favorites')),
    path('user/', include('user.urls', namespace='user')),
    path('order/', include('orders.urls', namespace='orders')),
    path('payment/', include('payment.urls', namespace='payment')),

    #api-endpoints
    path('api/v1/users/', include('user.api.user.urls')),
    path('api/v1/shop/', include('shop.api.shop.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)