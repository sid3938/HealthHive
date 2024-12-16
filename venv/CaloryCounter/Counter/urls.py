from django.urls import path
from .views import FoodItemSearch

urlpatterns = [
    path('food-item-search/', FoodItemSearch.as_view(), name='food-item-search'),
]
