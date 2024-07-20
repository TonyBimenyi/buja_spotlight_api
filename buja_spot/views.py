from django.shortcuts import render
from rest_framework import viewsets, mixins
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework import filters

from rest_framework import status
from django.http import HttpResponse

from .serializers import *

# class TokenPairView(TokenObtainPairView):
#     serializer_class = TokenPairSerializer

class LoginView(APIView):
    def post(self, request):

class RegisterView(APIView):
    serializer_class = RegisterSerializer
    permission_classes = AllowAny,

    def post(self, request, format=None):
        # serializer = RegisterSerializer(data=request)

        first_name = request.data['first_name']
        last_name = request.data['last_name']
        password = request.data['password']
        email = request.data['email']

        user_obj = User(
            username = email,
            first_name = first_name,
            last_name = last_name,
        )
        user_obj.set_password(password)
        user_obj.email = email
        user_obj.save()

        return Response({'status':'Succes'}, 201)

class GroupView(viewsets.ModelViewSet):
    serializer_class = GroupSerializer
    permission_classes = AllowAny
    queryset = Group.objects.all()
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