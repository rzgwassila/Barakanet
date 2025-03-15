# filepath: /home/camatchoo/WebDev/Dcf-hackathon/backend/users/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, CharityFileViewSet, CharityImageViewSet
from . import views

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'charity-files', CharityFileViewSet, basename='charity-files')
router.register(r'charity-images', CharityImageViewSet, basename='charity-images')

urlpatterns = [
    path('', include(router.urls)),
    path('register/', views.register_user, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('profile/', views.get_user_profile, name='profile'),
]