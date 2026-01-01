from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')

    first_name = models.CharField(max_length=50)          # required
    last_name = models.CharField(max_length=50)           # required
    phone = models.CharField(max_length=15)               # required

    age = models.PositiveIntegerField(null=True, blank=True)
    gender = models.CharField(max_length=10,
    choices=[
            ('male', 'Male'),
            ('female', 'Female'),
            ('other', 'Other')
        ],
        blank=True
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
