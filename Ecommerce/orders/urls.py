from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .  import views
urlpatterns = [
    path('cart',views.cart,name='cart'),
    path('add_to_cart', views.add_to_cart,name="add_to_cart"),
    
    
    
]