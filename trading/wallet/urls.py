from django.urls import path
from . import views

urlpatterns = [
    path('', views.cart_summary, name='wallet_summary'),
    path('add/', views.cart_add, name='wallet_add'),
    path('delete/', views.cart_delete, name='wallet_delete'),
    path('update/', views.cart_update, name='wallet_update'),
]