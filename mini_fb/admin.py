# File: mini_fb/admin.py
# Author: Steven Phung (sphung01@bu.edu), 5/27/2025
# Description: This is where we would register
# a model to the admin
from django.contrib import admin

# Register your models here.
from .models import Profile, StatusMessage
admin.site.register(Profile) # Registers the Profile model
admin.site.register(StatusMessage) # Registers the StatusMessage model
