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
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    image = models.CharField(max_length=255)
    pizzas = models.ManyToManyField(Pizza)
    soda = models.ForeignKey(Sodas, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class LunchOffer(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    image = models.CharField(max_length=255)
    pizzas = models.ManyToManyField(Pizza)
    soda = models.ForeignKey(Sodas, on_delete=models.CASCADE)
    breadsticks = models.ForeignKey(Breadsticks, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class TwoForOne(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    image = models.CharField(max_length=255)
    pizzas = models.ManyToManyField(Pizza)
    soda = models.ForeignKey(Sodas, on_delete=models.CASCADE)
    breadsticks = models.ForeignKey(Breadsticks, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
