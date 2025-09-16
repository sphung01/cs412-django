# File: mini_insta/admin.py
# Author: Steven Phung (sphung01@bu.edu), 9/16/2025
# Description: This is where we would register
# a model to the admin

from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Profile)