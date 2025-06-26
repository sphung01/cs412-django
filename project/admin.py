# File: project/admin.py
# Author: Steven Phung (sphung01@bu.edu), 6/25/2025
# Description: This is where we would register
# a model to the admin

from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(ProjectUser) # Registers the ProjectUser model
admin.site.register(Course) # Registers the Course model
admin.site.register(Enrollment) # Registers the Enrollment model
admin.site.register(Attendance) # Registers the Attendance model
admin.site.register(Report)# Registers the Report model