# File: voter_analytics/admin.py
# Author: Steven Phung (sphung01@bu.edu), 5/27/2025
# Description: This is where we would register
# model(s) to the admin.

from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Voter) # Registers the Voter model
