from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    TokenPairView, TokenRefreshView, RegisterView, ItemView,
    TicketTypeView, EventTypeView, EventCategoryView, EventView, EventTicketTypeView
)

router = DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('login/', TokenPairView.as_view(), name='login'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='register'),
    path('items/', ItemView.as_view({'get': 'list'}), name='item-list'),
    path('tickettypes/', TicketTypeView.as_view({'get': 'list'}), name='tickettype-list'),
    path('eventtypes/', EventTypeView.as_view({'get': 'list'}), name='eventtype-list'),
    path('eventcategories/', EventCategoryView.as_view({'get': 'list'}), name='eventcategory-list'),
    path('events/', EventView.as_view({'get': 'list'}), name='event-list'),
    path('eventtickettypes/', EventTicketTypeView.as_view({'get': 'list'}), name='eventtickettype-list'),
    path('api-auth/', include('rest_framework.urls')),
]
