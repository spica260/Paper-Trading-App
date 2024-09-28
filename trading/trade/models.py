from django.db import models

class Customer(models.Model):
    buyer = models.CharField(max_length=50)
    credit = models.DecimalField(default=0, decimal_places=2, max_digits=6)

    def __str__(self):
        return self.buyer
    
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(default=0, decimal_places=2, max_digits=6)

    def __str__(self):
        return self.name