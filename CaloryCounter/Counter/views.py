from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import FoodItem
from .serializers import FoodItemSerializer

class FoodItemSearch(APIView):
    def get(self, request, format=None):
        query = request.query_params.get('query', None)

        if query:
            food_items = FoodItem.objects.filter(name__icontains=query)
            if food_items.exists():
                serializer = FoodItemSerializer(food_items, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'No food items found for the given query.'}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({'error': 'Search query cannot be empty.'}, status=status.HTTP_400_BAD_REQUEST)
