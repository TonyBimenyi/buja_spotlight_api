from rest_framework import serializers
from .models import *
from django.db.models import fields

class TokenPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super(TokenPairSerializer, self).validate(attrs)
        data['is_admin'] = self.user.is_superuser
        data['groups'] = [x.name for x in self.user.groups.all()]
        data['username'] = self.user.username
        data['first_name'] = self.user.first_name
        data['last_name'] = self.user.last_name
        data['id'] = self.user.id

        return data


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        read_only_fields = 'is_active', 'is_staff',
        exclude = 'last_login', 'is_staff', 'date_joined', 'user_permission'

        extra_kwargs = {
            'username': {
                'validators': [UnicodeUsernameValidator()]
            }
        }

class RegisterSerializer(serializers.Serializer):
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    password = serializers.CharField(required=True)
    email = serializers.CharField(required=True)

class GroupSerializer(serializers.ModelField):
    class Meta:
        model =Group
        fields = '__all__'


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
