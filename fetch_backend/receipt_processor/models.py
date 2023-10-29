from django.db import models

class Receipt(models.Model):
    retailer = models.CharField(max_length = 255)
    purchaseDate = models.DateField()
    purchaseTime = models.TimeField()
    total = models.DecimalField(max_digits = 6, decimal_places = 2)

class Item(models.Model):
    receipt = models.ForeignKey(Receipt, related_name = 'items', on_delete = models.CASCADE)
    shortDescription = models.CharField(max_length = 255)
    price = models.DecimalField(max_digits = 6, decimal_places = 2)
