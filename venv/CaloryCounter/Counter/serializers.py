from rest_framework import serializers
from .models import FoodItem

class FoodItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodItem
        fields = ['id', 'name', 'serving_size', 'calories', 'carbohydrate', 
                  'cholesterol', 'total_fat', 'saturated_fat', 'fiber', 
                  'protein', 'sodium', 'sugars']
