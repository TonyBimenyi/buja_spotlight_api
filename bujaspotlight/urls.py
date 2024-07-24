from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from buja_spot import views

router = DefaultRouter()
# router.register(r'login', views.TokenPairView, basename='login')
router.register(r'items', views.ItemView, basename='item')
router.register(r'tickettypes', views.TicketTypeView, basename='tickettype')
router.register(r'eventtypes', views.EventTypeView, basename='eventtype')
router.register(r'eventcategories', views.EventCategoryView, basename='eventcategory')
router.register(r'events', views.EventView, basename='event')
router.register(r'eventtickettypes', views.EventTicketTypeView, basename='eventtickettype')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/auth/', include('buja_spot.urls')),  # Add this line to include app-specific URLs
]
