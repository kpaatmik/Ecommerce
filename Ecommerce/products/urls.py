from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .  import views
urlpatterns = [
    path('', views.index,name='home_page'),
    path('products_list', views.products,name='list_products'),
    path('product/<pk>', views.product_details,name='product_details'),
    path('cart',views.cart,name='cart')
]