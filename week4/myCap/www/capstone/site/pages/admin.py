from django.contrib import admin
from .models import Menu_Item, Service, ContactData, Carts, Side
# Register your models here.

admin.site.register(Menu_Item)
admin.site.register(Service)
admin.site.register(ContactData)
admin.site.register(Carts)
admin.site.register(Side)