from .wallet import Wallet

def wallet(request):
	return {'wallet': Wallet(request)}