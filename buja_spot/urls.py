from django.urls import path
from .views import ItemListCreate, ItemDetail, TicketTypeCreate,  TicketTypeDetail

urlpatterns = [
    path('items/', ItemListCreate.as_view(), name='item-list-create'),
    path('items/<int:pk>/', ItemDetail.as_view(), name='item-detail'),

    path('tickettypes/', TicketTypeCreate.as_view(), name='tickettype-list-create'),
    path('tickettypes/<int:pk>/', TicketTypeDetail.as_view(), name='tickettype-detail'),
]