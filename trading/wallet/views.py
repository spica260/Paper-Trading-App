from django.shortcuts import render, get_object_or_404
from trade.models import Customer, Product
from .wallet import Wallet
from django.http import JsonResponse

def wallet_summary(request):
    customer = Customer.objects.all()
    wallet = Wallet(request)
    wallet_products = wallet.get_prods
    quantities = wallet.get_quants
    totals = wallet.wallet_total()
    return render(request, "wallet_summary.html", {'wallet_products':wallet_products, 'quantities':quantities, 'totals':totals, 'customer':customer})

def wallet_add(request):
    wallet = Wallet(request)

    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))
        product = get_object_or_404(Product, id=product_id)
        wallet.add(product=product, quantity=product_qty)
        wallet_quantity = wallet.__len__()

        response = JsonResponse({ 'qty': wallet_quantity })
        return response

def wallet_delete(request):
    wallet = Wallet(request)

    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        wallet.delete(product=product_id)

        response = JsonResponse({'product':product_id})
        return response

def wallet_update(request):
    wallet = Wallet(request)

    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))

        wallet.update(product=product_id, quantity=product_qty)

        response = JsonResponse({'qty':product_qty})
        return response