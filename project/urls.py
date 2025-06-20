# File: project/urls.py
# Author: Steven Phung (sphung01@bu.edu), 6/20/2025
# Description: This creates pathing to different pages
# within the project folder.

from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

"""
Configures URLs for the 'mini_fb' app

Routes:



"static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)"
This line serves all of the static files (CSS, Javascript, Images) to the project
during the deployment.
"""

# This 'app_name' is helpful and avoids user from
# navigating to a different app and built into Django's
# namespaced URL routing system. Due to both 'hw' and 'quotes'
# app that have same name of the HTML files, the user will accidentally
# go to another app. Common issue when using Django.
app_name = 'project'

urlpatterns = [
    path(r'', views.home, name="home"),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)