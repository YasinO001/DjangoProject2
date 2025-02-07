from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)  # Naam van het product
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Prijs
    stock = models.IntegerField()  # Aantal in voorraad
    description = models.TextField(blank=True, null=True)  # Beschrijving (optioneel)
    created_at = models.DateTimeField(auto_now_add=True)  # Automatisch veld voor aanmaakdatum

    def __str__(self):
        return self.name  # Geeft de naam van het product weer in admin
