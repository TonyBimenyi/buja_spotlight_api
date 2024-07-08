from django.shortcuts import render
from rest_framework import viewsets
from .models import Item
from .serializers import ItemSerializer
from rest_framework.response import Response
# Create your views here.

class ItemView(viewsets.ViewSet):
    queryset = Item.objects.all()
    
    def list(self, request):
        serializer = ItemSerializer(self.queryset, many=True)
        return Response(serializer.data)
