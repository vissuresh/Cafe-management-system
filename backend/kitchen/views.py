from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, generics

from .models import Category, Item
from .serializers import CategorySerializer, ItemSerializer

class CategoryListView(generics.ListCreateAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

class CategoryRUDView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

class ItemListView(generics.ListCreateAPIView):
    serializer_class = ItemSerializer
    queryset = Item.objects.all()

class ItemRUDView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ItemSerializer
    queryset = Item.objects.all()

class ItemByCategory(generics.ListAPIView):
    serializer_class = ItemSerializer
    
    def get_queryset(self):

        return Item.objects.filter(category_id=self.kwargs['pk'])