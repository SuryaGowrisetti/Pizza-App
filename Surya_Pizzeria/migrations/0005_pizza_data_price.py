# Generated by Django 3.1.2 on 2020-11-11 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Surya_Pizzeria', '0004_auto_20201111_1650'),
    ]

    operations = [
        migrations.AddField(
            model_name='pizza_data',
            name='price',
            field=models.CharField(default=True, max_length=10),
        ),
    ]