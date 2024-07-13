"""
URL configuration for bujaspotlight project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from buja_spot import views

router = DefaultRouter()
router.register(r"item", views.ItemView)
router.register(r"ticket_type", views.TicketTypeView)
router.register(r"event_type", views.EventTypeView)
router.register(r"event_category", views.EventCategoryView)
router.register(r"event", views.EventView)
router.register(r"event_ticket_type", views.EventTicketTypeView)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
