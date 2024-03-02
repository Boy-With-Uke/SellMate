from django.contrib import admin
from store.models import Product, Order, Cart, Type, Promotion

admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Cart)
admin.site.register(Type)
admin.site.register(Promotion)