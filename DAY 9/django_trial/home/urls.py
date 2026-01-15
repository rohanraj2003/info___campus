from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.home),
    path('secondpage/', views.secondpage),
    path('base', views.base),
    path('index', views.index),
    path('customer', views.customer)
]