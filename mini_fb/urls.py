# File: mini_fb/urls.py
# Author: Steven Phung (sphung01@bu.edu), 5/27/2025
# Description: This creates pathing to different pages
# within the mini_fb folder.

from django.urls import path
from .views import * #Adds all the view functions that exist
from django.conf.urls.static import static    ## add for static files
from django.conf import settings
from django.contrib.auth import views as auth_views


"""
Configures URLs for the 'mini_fb' app

Routes:
- /mini_fb/                                           -> Takes the user to a page with all profiles showing
- /mini_fb/show_all                                   -> Same as default link above
- /mini_fb/profile/<int:pk>                           -> A page that shows a specific profile with their own primary key
- /mini_fb/create_profile                             -> A page for the user to create new profile
- /mini_fb/profile/<int:pk>/create_status             -> A page to add new messages for specific profile
- /mini_fb/profile/<int:pk>/update                    -> A page to update the Profile instance
- /mini_fb/status/<int:pk>/delete                     -> A page to delete the StatusMessage instance
- /mini_fb/status/<int:pk>/update                     -> A page to update the StatusMessage instance
- /mini_fb/profile/<int:pk>/add_friend/<int:other_pk> -> When the friend is added, this will redirect user back to the Profile page
- /mini_fb/profile/<int:pk>/friend_suggestions        -> A page that displays all profiles that are suggested
- /mini_fb/profile/<int:pk>/news_feed                 -> A page that displays news feed of all messages
- /mini_fb/login                                      -> A login page to authenticate user
- /mini_fb/logout                                     -> Logs user out and returns to 'show_all_profiles' page


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
    path('show_all', ShowAllProfilesView.as_view(), name="show_all_profiles"),
    path('profile/<int:pk>', ShowProfilePageView.as_view(), name='profile'),
    path('create_profile', CreateProfileView.as_view(), name='create_profile'),
    path('profile/create_status', CreateStatusMessageView.as_view(), name='create_status'),
    path('profile/update', UpdateProfileView.as_view(), name='update_profile'),
    path('status/<int:pk>/delete', DeleteStatusMessageView.as_view(), name='delete_status'),
    path('status/<int:pk>/update', UpdateStatusMessageView.as_view(), name='update_status'),
    path('profile/add_friend/<int:other_pk>', AddFriendView.as_view(), name='add_friend'),
    path('profile/friend_suggestions', ShowFriendSuggestionsView.as_view(), name='friend_suggestions'),
    path('profile/news_feed', ShowNewsFeedView.as_view(), name='news_feed'),
    path('login/', auth_views.LoginView.as_view(template_name='mini_fb/login.html', 
                                                extra_context={'current_time': time.ctime()}), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='mini_fb:show_all_profiles'), name='logout'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)