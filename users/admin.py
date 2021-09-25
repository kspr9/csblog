from django.contrib import admin
from .models import Profile

# registering the 'Profile' model created in 'users/models.py' 
admin.site.register(Profile)