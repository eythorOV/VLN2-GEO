# Generated by Django 4.2 on 2023-05-07 17:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pizzatoppings',
            name='pizza',
        ),
        migrations.RemoveField(
            model_name='pizzatoppings',
            name='topping',
        ),
        migrations.DeleteModel(
            name='Pizza',
        ),
        migrations.DeleteModel(
            name='PizzaToppings',
        ),
        migrations.DeleteModel(
            name='Toppings',
        ),
    ]
