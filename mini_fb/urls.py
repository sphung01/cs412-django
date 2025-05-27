# File: quotes/urls.py
# Author: Steven Phung (sphung01@bu.edu), 5/20/2025
# Description: This creates pathing to different pages
# within the quotes folder.

from django.urls import path
from .views import ShowAllProfilesView, ShowProfilePageView
from django.conf.urls.static import static    ## add for static files
from django.conf import settings


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
app_name = 'mini_fb'

urlpatterns = [
    path('', ShowAllProfilesView.as_view(), name="show_all_profiles"),
    path('profile/<int:pk>', ShowProfilePageView.as_view(), name='profile'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)