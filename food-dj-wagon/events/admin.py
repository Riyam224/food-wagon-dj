from django.contrib import admin

# Register your models here.
from .models import OnSale ,Popular_items ,Featured_Restaurants

admin.site.register(OnSale)
admin.site.register(Popular_items)
admin.site.register(Featured_Restaurants)