from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_tags(value):
    if not all(tag.strip() for tag in value.split(',')):
        raise ValidationError(
            _('Each tag must be non-empty and separated by commas.'),
            params={'value': value},
        )


from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name
    
class TicketType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class EventType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class EventCategory(models.Model):
    name = models.CharField(max_length=100)
    event_type = models.ForeignKey(EventType, on_delete=models.CASCADE)

    def __str__(self):
         return f"{self.id} | {self.name} | {self.event_type}" 

class Event(models.Model):
    TITLE_MAX_LENGTH = 255
    
    title = models.CharField(max_length=TITLE_MAX_LENGTH)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event_time_start = models.DateTimeField()
    event_time_end = models.DateTimeField()
    image = models.ImageField(upload_to='event_images/', max_length=255, null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    organizer_name = models.CharField(max_length=TITLE_MAX_LENGTH)
    organizer_phone = models.CharField(max_length=8)
    organizer_address = models.CharField(max_length=TITLE_MAX_LENGTH)
    event_type = models.ForeignKey(EventType, on_delete=models.CASCADE)
    event_category = models.ForeignKey(EventCategory, on_delete=models.CASCADE)
    location_name = models.CharField(max_length=TITLE_MAX_LENGTH)
    complete_address = models.TextField()
    location_lat = models.FloatField()
    location_lon = models.FloatField()
    ticket_types = models.ManyToManyField(TicketType, through='EventTicketType')
    is_active = models.BooleanField(default=False)
    tags = models.CharField(max_length=255, validators=[validate_tags], null=True, blank=True)

    def __str__(self):
        return (
            f"Event("
            f"Title: {self.title}, "
            f"Start: {self.event_time_start}, "
            f"End: {self.event_time_end}, "
            f"Organizer Name: {self.organizer_name}, "
            f"Organizer Phone: {self.organizer_phone}, "
            f"Category: {self.event_category}, "
            f"Latitude: {self.location_lat}, "
            f"Longitude: {self.location_lon}"
            f")"
        )
    
class EventTicketType(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    ticket_type = models.ForeignKey(TicketType, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.event.title} - {self.ticket_type.name} - ${self.price}"


