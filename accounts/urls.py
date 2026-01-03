from django.urls import path
from .views import register_user, update_profile, change_password, get_profile

urlpatterns = [
    path('register/', register_user, name='register'),
    path('profile/', get_profile, name='profile'),
    path('profile_update/', update_profile, name='profile_update'),
    path('change_password/', change_password, name='change_password')
]