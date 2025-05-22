# File: quotes/urls.py
# Author: Steven Phung (sphung01@bu.edu), 5/20/2025
# Description: This creates pathing to different pages
# within the quotes folder.

from django.urls import path
from . import views
from django.conf.urls.static import static    ## add for static files
from django.conf import settings


"""
Configures URLs for the quotes app

Routes:
- /quotes/ -> Takes the user to the homepage where Quote of The Day is being displayed
- /quotes/quote -> Same as the URL above. Takes you to homepage
- /quotes/show_all -> Displays all quotes and images to user on this URL
- /quotes/about -> A brief description of the website to the user

"static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)"
This line serves all of the static files (CSS, Javascript, Images) to the project
during the deployment.
"""

# This 'app_name' is helpful and avoids user from
# navigating to a different app and built into Django's
# namespaced URL routing system. Due to both 'hw' and 'quotes'
# app that have same name of the HTML files, the user will accidentally
# go to another app. Common issue when using Django.
app_name = 'quotes'

urlpatterns = [
    path(r'', views.home_page, name="home"),
    path(r'quote', views.quote, name="quote"),
    path(r'show_all', views.show_all, name="show_all"),
    path(r'about', views.about, name="about"),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)