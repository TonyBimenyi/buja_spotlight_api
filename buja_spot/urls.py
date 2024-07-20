from django.urls import path, include
from .views import ItemListCreate, ItemDetail, TicketTypeCreate,  TicketTypeDetail, TokenPairView, TokenRefreshView,RegisterView,LoginView
from django.db import router

urlpatterns = [

    path('', include(router.urls)),
    path('login/', LoginView.as_view(), name='login'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='register'),
    path('items/', ItemListCreate.as_view(), name='item-list-create'),
    path('items/<int:pk>/', ItemDetail.as_view(), name='item-detail'),

    path('tickettypes/', TicketTypeCreate.as_view(), name='tickettype-list-create'),
    path('tickettypes/<int:pk>/', TicketTypeDetail.as_view(), name='tickettype-detail'),
    path('api-auth/', include('rest_framework.urls')),
]