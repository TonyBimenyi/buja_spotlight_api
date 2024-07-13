from django.shortcuts import render
from rest_framework import viewsets
from .models import Item,TicketType,EventType,EventCategory,Event,EventTicketType
from .serializers import ItemSerializer,TicketTypeSerializer,EventTypeSerializer, EventCategorySerializer, EventCategorySerializer, EventSerializer, EventTicketTypeSerializer
from rest_framework.response import Response
# Create your views here.

class ItemView(viewsets.ViewSet):
    queryset = Item.objects.all()
    
    def list(self, request):
        serializer = ItemSerializer(self.queryset, many=True)
        return Response(serializer.data)

class TicketTypeView(viewsets.ViewSet):
    queryset = TicketType.objects.all()

    def list(self, request):
        serializer = TicketTypeSerializer(self.queryset, many = True)
        return Response(serializer.data)

class EventTypeView(viewsets.ViewSet):
    queryset = EventType.objects.all()

    def list(self, request):
        serializer = EventTypeSerializer(self.queryset, many = True)
        return Response(serializer.data)

class EventCategoryView(viewsets.ViewSet):
    queryset = EventCategory.objects.all()

    def list(self, request):
        serializer = EventCategorySerializer(self.queryset, many = True)
        return Response(serializer.data)
    

class EventView(viewsets.ViewSet):
    queryset = Event.objects.all()

    def list(self, request):
        serializer = EventSerializer(self.queryset, many = True)
        return Response(serializer.data)
    
    
class EventTicketTypeView(viewsets.ViewSet):
    queryset = EventTicketType.objects.all()

    def list(self, request):
        serializer = EventTicketTypeSerializer(self.queryset, many = True)
        return Response(serializer.data)