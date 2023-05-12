from django.db import models
from menu.models import Pizza

class Sodas(models.Model):
    name = models.CharField(max_length=50)
    image = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class Breadsticks(models.Model):
    name = models.CharField(max_length=50)
    image = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class SpecialOffer(models.Model):
    name = models.CharField(max_length=100, default='Special Offer')
    description = models.TextField(default='Pizza, breadsticks, and soda - great value, great taste.')
    price = models.IntegerField(default=2990)
    image = models.CharField(max_length=255, default='https://i.ibb.co/HKjn1zt/Special-offer.png')
    pizzas = models.ForeignKey(Pizza, on_delete=models.CASCADE, null=True, blank=True)
    soda = models.ForeignKey(Sodas, on_delete=models.CASCADE, null=True, blank=True)
    breadsticks = models.ForeignKey(Breadsticks, on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return self.name

class LunchOffer(models.Model):
    name = models.CharField(max_length=100, default='Lunch Offer')
    description = models.TextField(default='Pizza and soda - great value, great taste.')
    price = models.IntegerField(default=2490)
    image = models.CharField(max_length=255, default='https://i.ibb.co/0jJQY1Q/Lunch-offer.png')
    pizzas = models.ForeignKey(Pizza, on_delete=models.CASCADE, null=True, blank=True)
    soda = models.ForeignKey(Sodas, on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return self.name

class TwoForOne(models.Model):
    name = models.CharField(max_length=100, default='Two for One')
    description = models.TextField(default='Two pizzas for the price of one - great value, great taste.')
    price = models.IntegerField(default=3990)
    image = models.CharField(max_length=255, default='https://i.ibb.co/4SNhHp0/2-for-1.png')
    pizza1 = models.ForeignKey(Pizza, on_delete=models.CASCADE, null=True, blank=True, related_name='pizza1')
    pizza2 = models.ForeignKey(Pizza, on_delete=models.CASCADE, null=True, blank=True, related_name='pizza2')
    soda = models.ForeignKey(Sodas, on_delete=models.CASCADE, null=True, blank=True)
    breadsticks = models.ForeignKey(Breadsticks, on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return self.name