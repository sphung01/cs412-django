# File: cs412/urls.py
# Author: Steven Phung (sphung01@bu.edu), 5/20/2025
# Description: This file is responsible for creating routes
# in the URL. The "urlpatterns" contain paths that leads
# to different projects.

"""
URL configuration for cs412 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
import hw
import quotes

"""
URL configuration

Routes:
- /admin/               -> Paths to the "admin" interface
- /hw/                  -> Paths to the "hw" example with URLs included
- /formdata/            -> Paths to the "formdata" example with URLs included
- /blog/                -> Paths to the "blog" example with URLs included
- /marathon_analytics/  -> Paths to the "marathon_analytics" example with URLs included
- /quotes/              -> Paths to the "quotes" website with URLs included
- /restaurant/          -> Paths to the "restaurant" app with URLs included
- /mini_fb/             -> Paths to the "mini_fb" app with URLs included
- /voter_analytics/     -> Paths to the "voter_analytics" website with URLs included
- /project/             -> Paths to the "project" website with URLs included
"""
urlpatterns = [
    path("admin/", admin.site.urls),
    path("hw/", include("hw.urls")),
    path("formdata/", include("formdata.urls")), 
    path("blog/", include("blog.urls")),
    path("marathon_analytics/", include("marathon_analytics.urls")),
    path("quotes/", include("quotes.urls")),
    path("restaurant/", include("restaurant.urls")),
    path("mini_fb/", include("mini_fb.urls")),
    path("voter_analytics/", include("voter_analytics.urls")),
    path("project/", include("project.urls")),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
