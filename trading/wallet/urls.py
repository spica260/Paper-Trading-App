from django.urls import path
from . import views

urlpatterns = [
    path('', views.wallet_summary, name='wallet_summary'),
    path('add/', views.wallet_add, name='wallet_add'),
    path('delete/', views.wallet_delete, name='wallet_delete'),
    path('update/', views.wallet_update, name='wallet_update'),
]