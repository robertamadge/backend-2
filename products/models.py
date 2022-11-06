from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    price = models.DecimalField(max_digits=100, decimal_places=2)
    expiration_date = models.DateField()

    def __str__(self) -> str:
        return self.name