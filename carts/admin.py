from django.contrib import admin

from .models import CartProduct, Cart


admin.site.register(Cart)
admin.site.register(CartProduct)
