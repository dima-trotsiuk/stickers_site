# Generated by Django 4.0.3 on 2022-03-31 18:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0004_alter_stickersmain_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='stickersdima',
            options={'verbose_name': 'Склад Діми'},
        ),
        migrations.AlterModelOptions(
            name='stickersvlad',
            options={'verbose_name': 'Склад Влада'},
        ),
    ]
