from django.contrib import admin
from .models import Item,TicketType,EventType,EventCategory,Event,EventTicketType
# Register your models here.
admin.site.register(Item)
admin.site.register(TicketType)
admin.site.register(EventType)
admin.site.register(EventCategory)
admin.site.register(Event)
admin.site.register(EventTicketType)

