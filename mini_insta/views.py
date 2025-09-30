# File: mini_insta/views.py
# Author: Steven Phung (sphung01@bu.edu), 9/16/2025
# Description: In this file, we create view functions
# to send back a response to the client. Such as
# displaying the appropriate template on the web

from django.shortcuts import render
from .models import * 
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
import random
import time

class ProfileListView(ListView):
    """
        This subclass will take in a 'ListView' and display
        all of the Profiles that exist in the database
    """
    
    # Retrieves the objects of Profile type from database
    model = Profile

    # Takes an appropriate template to display to user
    template_name = 'mini_insta/show_all_profiles.html'

    # A context name we'll use to find data in the template
    context_object_name = 'profiles'

    # When using a subclass to pass contexts,
    # we have to create a function within it.
    def get_context_data(self, **kwargs):
        """
            Passes over one OR multiple contexts to the HTML template
        """
        context = super().get_context_data()

        context['current_time'] = time.ctime()

        return context

class ProfileDetailView(DetailView):
    """
        This will display ONE profile since that is what
        DetailView is for
    """

    # Retrieves the objects of Profile type from database
    model = Profile

    # We need an appropriate template that will display a Profile
    # depending on the primary key number
    template_name = 'mini_insta/show_profile.html'

    # We give a specific context name for the object
    # grabbed from the database
    context_object_name = 'profile'

    # In this function, we can add as many
    # contexts as we want for HTML to use
    def get_context_data(self, **kwargs):
        """
            Passes over one OR multiple contexts to the HTML template
        """
        context = super().get_context_data()

        context['current_time'] = time.ctime()

        return context
    
class PostDetailView(DetailView):
    """
        This will display ONE post from a specific profile
    """

    # Retrieves the objects of Post type from database
    model = Post

    template_name = 'mini_insta/show_post.html'

    context_object_name = 'post'