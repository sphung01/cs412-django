from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(ProjectUser)
admin.site.register(Course) 
admin.site.register(Enrollment) 
admin.site.register(Attendance) 
admin.site.register(Report)