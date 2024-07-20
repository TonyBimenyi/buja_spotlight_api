from django.urls import path, include
from .views import ItemListCreate, ItemDetail, TicketTypeCreate,  TicketTypeDetail, TokenPairView, TokenRefreshView,RegisterView
from django.db import router

urlpatterns = [

    path('', include(router.urls)),
    path('login/', TokenPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    path('register/', RegisterView.as_view()),
    path('items/', ItemListCreate.as_view(), name='item-list-create'),
    path('items/<int:pk>/', ItemDetail.as_view(), name='item-detail'),

    path('tickettypes/', TicketTypeCreate.as_view(), name='tickettype-list-create'),
    path('tickettypes/<int:pk>/', TicketTypeDetail.as_view(), name='tickettype-detail'),
    path('api-auth/', include('rest_framework.urls')),
]