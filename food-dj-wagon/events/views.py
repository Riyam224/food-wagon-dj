from django.shortcuts import render

# Create your views here.
from .models import OnSale , Popular_items , Featured_Restaurants


def index(request):
    sales = OnSale.objects.all()
    items = Popular_items.objects.all()
    restaurants = Featured_Restaurants.objects.all()

    # todo search popular items 
    popular_items = request.GET.get('search-food')
    if popular_items != ''  and popular_items is not None:
        items = items.filter(name__icontains=popular_items)

    # todo search by featured_restaurants
    find_food = request.GET.get('find_food')
    if find_food != '' and find_food is not None:
        restaurants = restaurants.filter(name__icontains=find_food)
    context = {
        'sales' :  sales, 
        'items': items,
        'restaurants': restaurants
    }
    return render(request , 'index.html' , context)