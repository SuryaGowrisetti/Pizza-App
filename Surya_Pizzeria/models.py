from django.db import models

# Create your models here.
class Pizza_Data(models.Model):
    pizza_name = models.CharField(max_length=50)
    pizza_price = models.CharField(max_length=10)


