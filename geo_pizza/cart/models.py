from django.db import models
from menu.models import Pizza
from offers.models import SpecialOffer, LunchOffer, TwoForOne
from django.contrib.auth.models import User

class Cart(models.Model):
    total_price = models.DecimalField(max_digits=10, decimal_places=0, default=0)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'Cart for {self.user.username}'

    def calculate_total_price(self):
        total_price = 0
        for cart_item in self.cart_items.all():
            print(cart_item.total_price())
            total_price += cart_item.total_price()
        self.total_price = total_price
        
        return total_price

    def save(self, *args, **kwargs):
        # print('in Cart save')
        # if self.cartitem_set.all():
        #     print('cartitem_set exists')
        #     self.total_price = self.calculate_total_price()
        super().save(*args, **kwargs)



class CartItem(models.Model):
    product_type_choices = [
        ('Pizza', 'Pizza'),
        ('SpecialOffer', 'Special Offer'),
        ('LunchOffer', 'Lunch Offer'),
        ('TwoForOne', 'Two for One')
    ]
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, null=True, blank=True, related_name='cart_items')
    product_type = models.CharField(max_length=20, choices=product_type_choices)
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE, null=True, blank=True)
    special_offer = models.ForeignKey(SpecialOffer, on_delete=models.CASCADE, null=True, blank=True)
    lunch_offer = models.ForeignKey(LunchOffer, on_delete=models.CASCADE, null=True, blank=True)
    two_for_one = models.ForeignKey(TwoForOne, on_delete=models.CASCADE, null=True, blank=True)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        if self.pizza:
            return f'{self.pizza.name} ({self.quantity})'
        elif self.special_offer:
            return f'{self.special_offer.name} ({self.quantity})'
        elif self.lunch_offer:
            return f'{self.lunch_offer.name} ({self.quantity})'
        elif self.two_for_one:
            return f'{self.two_for_one.name} ({self.quantity})'
        else:
            return 'Cart item'

    def total_price(self):
        if self.pizza:
            return self.pizza.price * self.quantity
        elif self.special_offer:
            return self.special_offer.price * self.quantity
        elif self.lunch_offer:
            return self.lunch_offer.price * self.quantity
        elif self.two_for_one:
            return self.two_for_one.price * self.quantity
        else:
            return 0