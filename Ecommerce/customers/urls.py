from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .  import views
urlpatterns = [
    path('customer', views.account,name='accout_details'),
    path('log_out', views.sign_out,name='log_out')

]