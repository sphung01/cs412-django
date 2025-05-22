# File: restaurant/urls.py
# Author: Steven Phung (sphung01@bu.edu), 5/22/2025
# Description: This creates pathing to different pages
# within the restaurant folder.

from django.urls import path
from . import views
from django.conf.urls.static import static    ## add for static files
from django.conf import settings


"""
Configures URLs for the 'restaurant' app

Routes:
- /restaurant/             -> Takes the user to the main page of the restaurant
- /restaurant/main         -> Same as the route above. Takes user to the main page.
- /restaurant/order        -> Displays the menu/form to the user
- /restaurant/confirmation -> Takes user to the confirmation page after submitting form

"static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)"
This line serves all of the static files (CSS, Javascript, Images) to the project
during the deployment.
"""

# This 'app_name' is helpful and avoids user from
# navigating to a different app and built into Django's
# namespaced URL routing system. If there are apps that have the same HTML file name, 
# the user will accidentally go to another app. 
# Common issue when using Django.
app_name = 'restaurant'


# Paths to 4 different url routes.
urlpatterns = [
    path(r'', views.main, name="home"),
    path(r'main', views.main, name="main"),
    path(r'order', views.order, name="order"),
    path(r'confirmation', views.confirmation, name="confirmation"),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)