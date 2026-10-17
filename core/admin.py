from django.contrib import admin
from .models import Users, Products, Categories, Orders, OrderItems, Payments, Cart, Reviews

admin.site.register(Users)
admin.site.register(Products)
admin.site.register(Categories)
admin.site.register(Orders)
admin.site.register(OrderItems)
admin.site.register(Payments)
admin.site.register(Cart)
admin.site.register(Reviews)