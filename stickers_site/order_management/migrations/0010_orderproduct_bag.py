# Generated by Django 4.0.3 on 2022-04-05 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order_management', '0009_remove_orderproduct_bag'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderproduct',
            name='bag',
            field=models.BooleanField(default=True, verbose_name='В корзині?'),
        ),
    ]
