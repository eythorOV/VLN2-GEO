
from django.db import models

class Toppings(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()

    def __str__(self):
        return self.name

class Pizza(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    spicy = models.BooleanField()
    vegan = models.BooleanField()
    desert = models.BooleanField()
    popular = models.BooleanField()
    image = models.CharField(max_length=255)
    description = models.TextField()
    long_description = models.TextField(null=True)
    toppings = models.ManyToManyField(Toppings)

    def __str__(self):
        return f"{self.name}, {self.priceSmall}, {self.priceMedium}, {self.priceLarge}, {self.image}, {self.toppings} {self.description}"