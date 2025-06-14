# File: voter_analytics/urls.py
# Author: Steven Phung (sphung01@bu.edu), 6/12/2025
# Description: This creates pathing to different pages
# within the voter_analytics folder.

from django.urls import path
from .views import * #Adds all the view functions that exist
from django.conf.urls.static import static    ## add for static files
from django.conf import settings

"""
Configures URLs for the 'voter_analytics' app

Routes:
- /voter_analytics/                                   -> Displays 100 voters on each page
- /voter_analytics/voters                             -> Displays 100 voters on each page and with filter
- /voter_analytics/voter/<int:pk>                     -> A page displays one voter that was clicked on
- /voter_analytics/graphs                             -> A page that displays the graph of all of the voters

"static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)"
This line serves all of the static files (CSS, Javascript, Images) to the project
during the deployment.
"""

# This 'app_name' is helpful and avoids user from
# navigating to a different app and built into Django's
# namespaced URL routing system. Due to both 'hw' and 'quotes'
# app that have same name of the HTML files, the user will accidentally
# go to another app. Common issue when using Django.
app_name = 'voter_analytics'

urlpatterns = [
    path(r'', VotersListView.as_view(), name='home'),
    path(r'voters', VotersListView.as_view(), name='voters_list'),
    path(r'voter/<int:pk>', VoterDetailView.as_view(), name='voter'),
    path(r'graphs', VotersGraphListView.as_view(), name='graphs'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)