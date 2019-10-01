from django.contrib import admin
from .models import Product, Category


class ProductAdmin(admin.ModelAdmin):
    search_fields = ('name', )
    list_filter = ('category', 'created', 'modified')
    list_display = ('uuid', 'name', 'category', 'modified', 'created')


class CategoryAdmin(admin.ModelAdmin):
    search_fields = (
        'name',
        'code',
    )
    list_filter = ('created', 'modified')
    list_display = ('code', 'name', 'created', 'modified')


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.site_header = 'Inventory System'
