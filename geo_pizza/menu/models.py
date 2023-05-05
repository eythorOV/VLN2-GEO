from django.db import models


class Pizza(models.Model):
    name = models.CharField(max_length=100)
    priceSmall = models.IntegerField()
    priceMedium = models.IntegerField()
    priceLarge = models.IntegerField()
    spicy = models.BooleanField(default=False)
    vegan = models.BooleanField(default=False)
    desert = models.BooleanField(default=False)
    popular = models.BooleanField(default=False)
    image = models.ImageField(upload_to='pizza_images')
    description = models.TextField()

    def __str__(self):
        return f"{self.name}, {self.priceSmall}, {self.priceMedium}, {self.priceLarge}, {self.image}, {self.description}"

class Toppings(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    def __str__(self):
        return self.name

class PizzaToppings(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE, related_name='pizza_toppings')
    topping = models.ForeignKey('Toppings', on_delete=models.CASCADE, related_name='pizza_toppings')