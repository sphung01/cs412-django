# File: project/urls.py
# Author: Steven Phung (sphung01@bu.edu), 6/20/2025
# Description: This creates pathing to different pages
# within the project folder.

from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import * #Adds all the view functions that exist
from django.contrib.auth import views as auth_views

"""
Configures URLs for the 'mini_fb' app

Routes:
- /project/ -> The home page of the website
- /project/login -> The login page for user to be authenticated
- /project/logout -> Logs the user out and redirects to home page
- /project/signup -> Allows the user to create new account


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
    path('login/', auth_views.LoginView.as_view(template_name='project/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='project:home'), name='logout'),
    path('signup/', CreateUserView.as_view(), name='sign_up'),
    path('account/<int:pk>', ShowAccountView.as_view(), name='account'),
    path('courses/', ShowCoursesView.as_view(), name='courses'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)