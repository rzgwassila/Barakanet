from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    UserViewSet, LocationViewSet, VolunteerViewSet,
    CharitableOrganizationViewSet, PhotoViewSet,
    EventViewSet, VolunteerRequestViewSet, VolunteerHistoryViewSet
)

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'locations', LocationViewSet)
router.register(r'volunteers', VolunteerViewSet)
router.register(r'organizations', CharitableOrganizationViewSet)
router.register(r'photos', PhotoViewSet)
router.register(r'events', EventViewSet)
router.register(r'volunteer-requests', VolunteerRequestViewSet)
router.register(r'volunteer-history', VolunteerHistoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls')),
]