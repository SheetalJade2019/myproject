from tkinter import CASCADE
from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100)
    stripe_product_id = models.CharField(max_length=100)

    def __str__(self):
        print(super().__str__())
        return self.name

class Price(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    stripe_price_id = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    file = models.FileField(upload_to="product_files/", blank=True, null=True)
    url = models.URLField(default="")

    def get_display_price(self):
        return "{0:.2f}".format(self.price / 100)