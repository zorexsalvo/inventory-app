from django.contrib import admin
from .models import Product, Category


admin.site.register(Product)
admin.site.register(Category)
admin.site.site_header = 'Inventory System'
