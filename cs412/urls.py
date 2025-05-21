# File: cs412/urls.py
# Author: Steven Phung (sphung01@bu.edu), 5/20/2025
# Description: This file is responsible for creating routes
# for the website. 

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
import hw
import quotes

urlpatterns = [
    path("admin/", admin.site.urls),
    path("hw/", include("hw.urls")),
    path("quotes/", include("quotes.urls")),
]
