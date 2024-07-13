from rest_framework import serializers
from .models import Item,TicketType,EventType,EventCategory,Event,EventTicketType

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model=Item
        fields = '__all__'

c