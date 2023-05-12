# Generated by Django 4.2.1 on 2023-05-12 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offers', '0002_remove_twoforone_pizzas_twoforone_pizza1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='specialoffer',
            name='description',
            field=models.TextField(default='Pizza, breadsticks, and soda - great value, great taste.'),
        ),
        migrations.AlterField(
            model_name='specialoffer',
            name='image',
            field=models.CharField(default='https://i.ibb.co/HKjn1zt/Special-offer.png', max_length=255),
        ),
        migrations.AlterField(
            model_name='specialoffer',
            name='name',
            field=models.CharField(default='Special Offer', max_length=100),
        ),
        migrations.AlterField(
            model_name='specialoffer',
            name='price',
            field=models.IntegerField(default=2990),
        ),
    ]