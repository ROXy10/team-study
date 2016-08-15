from django.contrib import admin
from .models import Pizza, Client, Phone, Address, Order, Bonus, Courier, OrderTable

admin.site.register(Pizza)
admin.site.register(Client)
admin.site.register(Phone)
admin.site.register(Bonus)
admin.site.register(Order)
admin.site.register(Address)
admin.site.register(Courier)
admin.site.register(OrderTable)
