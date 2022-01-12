from django.db import models
from django.db.models.enums import Choices

# Create your models here.
from django.utils.translation import ugettext_lazy as _

class OnSale(models.Model):
    name = models.CharField(_("name"), max_length=50)
    image = models.ImageField(_("image"), upload_to='onsale')
    discount = models.IntegerField(_("discount"))
    remaining_days = models.IntegerField(_("remaining days"))
    

    class Meta:
        verbose_name = _("OnSale")
        verbose_name_plural = _("OnSales")

    def __str__(self):
        return self.name

RESTAURANTS_CHOICES = [
    ('BA' , 'Burger Arena'),
    ('TS' , 'Top Sticks'),
    ('CW' , 'Cake World'),
    ('FD' ,'Fastfood Dine'),
    ('FM' , 'Foody Man')
]
# todo search by popular items name 

class Popular_items(models.Model):
    name = models.CharField(_("name"), max_length=50)
    image = models.ImageField(_("image"), upload_to='popular_items')
    price = models.DecimalField(_("price"), max_digits=5, decimal_places=2)
    restaurants = models.CharField(_("restaurants"), choices=RESTAURANTS_CHOICES ,  max_length=2)


    class Meta:
        verbose_name = _("Popular_items")
        verbose_name_plural = _("Popular_itemss")

    def __str__(self):
        return self.name


DELIVERED_STATUS = [
    ('Fast' , 'fast'),
    ('Medium' , 'medium'),
    ('Slow' , 'slow')
]

OPENING_STATUS = [
    ('Tomorrow' , 'Opens_Tomorrow'),
    ('Now' , 'Opens_Now'),
]

# todo search for restaurants 
class Featured_Restaurants(models.Model):
    name = models.CharField(_("name"), max_length=50)
    discount = models.IntegerField(_("discount"))
    delivered_status = models.CharField(_("delivered status"), choices=DELIVERED_STATUS,max_length=10)
    image = models.ImageField(_("image"), upload_to='featured_restaurants')
    logo_img = models.ImageField(_("logo image"), upload_to='featured_logo')
    opening_status = models.CharField(_("opening status"), choices=OPENING_STATUS , max_length=10)


    

    class Meta:
        verbose_name = _("Featured_Restaurants")
        verbose_name_plural = _("Featured_Restaurantss")

    def __str__(self):
        return self.name

   