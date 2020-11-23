from django.contrib import admin
from .models import Product, Sub_Category, Category
# Register your models here.

admin.site.register(Product)
admin.site.register(Sub_Category)
admin.site.register(Category)