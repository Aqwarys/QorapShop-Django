from django.urls import path
from . import views

app_name = 'shop'
urlpatterns = [
    path('', views.home_page, name='home'),
    path('category/<slug:slug>', views.catefory_page, name='category'),
    path('<slug:slug>', views.product_detail, name='product_detail'),
]
