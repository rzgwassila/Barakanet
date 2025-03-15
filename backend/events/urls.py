# filepath: /home/camatchoo/WebDev/Dcf-hackathon/backend/events/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EventViewSet, RequestViewSet

router = DefaultRouter()
router.register(r'events', EventViewSet)
router.register(r'requests', RequestViewSet)

urlpatterns = [
    path('', include(router.urls)),
]