from django.contrib import admin
from .models import Product  # Importeer het model

# Registreer het Product-model in de admin
admin.site.register(Product)
