# Generated by Django 4.0.3 on 2022-04-10 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bag', '0004_alter_bagproduct_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bag',
            name='price',
            field=models.IntegerField(default=0, verbose_name='Сума'),
        ),
        migrations.AlterField(
            model_name='bag',
            name='ttn',
            field=models.CharField(default=0, max_length=255, verbose_name='ТТН'),
        ),
    ]
