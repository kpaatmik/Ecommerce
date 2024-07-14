from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .  import views
urlpatterns = [
    path('', views.index),
    path('products_list', views.products,name='list_products'),
    path('product', views.product_details,name='product_details'),
]