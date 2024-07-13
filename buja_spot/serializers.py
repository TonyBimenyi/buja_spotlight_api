from rest_framework import serializers
from .models import Item,TicketType,EventType,EventCategory,Event,EventTicketType

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model=Item
        fields = '__all__'

class TicketTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketType
        fields = '__all__'

class EventTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventType
        fields = '__all__'

class EventCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = EventCategory
        fields = '__all__'


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

class EventTicketTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventTicketType
        fields = '__all__'
