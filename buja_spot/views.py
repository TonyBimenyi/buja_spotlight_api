from django.shortcuts import render
from rest_framework import viewsets
from .models import Item,TicketType,EventType,EventCategory,Event,EventTicketType
from .serializers import ItemSerializer
from rest_framework.response import Response
# Create your views here.

class ItemView(viewsets.ViewSet):
    queryset = Item.objects.all()
    
    def list(self, request):
        serializer = ItemSerializer(self.queryset, many=True)
        return Response(serializer.data)

class TicketTypeView(viewsets.ViewSet):
    queryset = TicketType.objects.all()

