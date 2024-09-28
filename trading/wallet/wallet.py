from trade.models import Product

class Wallet():
    def __init__(self, request):
        self.session = request.session
        wallet = self.session.get('session_key')

        if 'session_key' not in request.session:
            wallet = self.session['session_key'] = {}

        self.wallet = wallet

    def add(self, product, quantity):
        product_id = str(product.id)
        product_qty = str(quantity)

        if product_id in self.wallet:
            pass
        else:
            self.wallet[product_id] = int(product_qty)

        self.session.modified = True

    def __len__(self):
        return len(self.wallet)
    
    def get_prods(self):
        product_ids = self.wallet.keys()
        products = Product.objects.filter(id__in=product_ids)
        return products

    def get_quants(self):
        quantities = self.wallet
        return quantities
    
    def update(self, product, quantity):
        product_id = str(product)
        product_qty = int(quantity)
        ourwallet = self.wallet
        ourwallet[product_id] = product_qty

        self.session.modified = True

        thing = self.wallet
        return thing
    
    def delete(self, product):
        product_id = str(product)
        if product_id in self.wallet:
            del self.wallet[product_id]

        self.session.modified = True

    def wallet_total(self):
            product_ids = self.wallet.keys()
            products = Product.objects.filter(id__in=product_ids)
            quantities = self.wallet
            total = 0
            for key, value in quantities.items():
                key = int(key)
                for product in products:
                    if product.id == key:
                        total = total + (product.price * value)
                        if total > int(500):
                            return 'Insufficient credit'
                        else:
                            pass
            return total