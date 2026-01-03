from django.urls import path
from .views import register_user, update_profile, change_password, logout_user, get_profile

urlpatterns = [
    path('register/', register_user, name='register'),
    path('profile/', get_profile, name='profile')
]