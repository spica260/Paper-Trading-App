from django.shortcuts import render
from trade.models import Customer

def wallet_summary(request):
    customer = Customer.objects.all()
    return render(request, "wallet_summary.html", {'customer':customer})

def wallet_add(request):
    pass

def wallet_delete(request):
    pass

def wallet_update(request):
    pass