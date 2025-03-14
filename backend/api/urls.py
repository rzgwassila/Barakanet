from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (UserViewSet, CharityEventViewSet, ItemRequestViewSet,
                   VolunteerApplicationViewSet, ItemLendingViewSet)

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'events', CharityEventViewSet)
router.register(r'item-requests', ItemRequestViewSet)
router.register(r'applications', VolunteerApplicationViewSet)
router.register(r'lendings', ItemLendingViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
]