from django.db import models
from django.contrib.auth.models import User

class Cart(models.Model):
    pizzas = models.ManyToManyField('Pizza', blank=True)
    offers = models.ManyToManyField('Offer', blank=True)
    def __str__(self):
        return f"Cart #{self.id} - {self.user.username}"