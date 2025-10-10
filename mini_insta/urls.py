# File: mini_insta/urls.py
# Author: Steven Phung (sphung01@bu.edu), 9/16/2025
# Description: This creates pathing to different pages
# within the mini_insta folder.

from django.urls import path
from .views import * #Adds all the view functions that exist
from django.conf.urls.static import static    ## add for static files
from django.conf import settings
from django.contrib.auth import views as auth_views

app_name = 'mini_insta'

urlpatterns = [
    path('', ProfileListView.as_view(), name="show_all_profiles"),
    path('show_all', ProfileListView.as_view(), name="show_all_profiles"),
    path('profile/<int:pk>', ProfileDetailView.as_view(), name="show_profile"),
    path('profile/<int:pk>/create_post', CreatePostView.as_view(), name='create_post'),
    path('profile/<int:pk>/update', UpdateProfileView.as_view(), name='update_profile'),
    path('post/<int:pk>', PostDetailView.as_view(), name='show_post'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)