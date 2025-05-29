# File: mini_fb/views.py
# Author: Steven Phung (sphung01@bu.edu), 5/27/2025
# Description: In this file, we create view functions
# to send back a response to the client. Such as
# displaying the appropriate template on the web

from django.shortcuts import render
from .models import Profile 
from .forms import CreateProfileForm
from django.views.generic import ListView, DetailView, CreateView
import random
import time

class ShowAllProfilesView(ListView):
    """
        This subclass will take in a 'ListView' and display
        all of the Profiles that exist in the database
    """
    
    # Retrieves the objects of Profile type from database
    model = Profile

    # Takes an appropriate template to display to user
    template_name = 'mini_fb/show_all_profiles.html'

    # A context name we'll use to find data in the template
    context_object_name = 'profiles'

    # When using a subclass to pass contexts,
    # we have to create a function within it.
    def get_context_data(self, **kwargs):
        context = super().get_context_data()

        context['current_time'] = time.ctime()

        return context

class ShowProfilePageView(DetailView):
    """
        Show the details for one profile
    """

    # Retrieves the objects of Profile type from database
    model = Profile

    # Takes an appropriate template to display to user
    template_name = 'mini_fb/show_profile.html' ## reusing same template!!

    # A context name we'll use to find data in the template
    context_object_name = 'profile'

    # Get the current time for footer
    def get_context_data(self, **kwargs):
        context = super().get_context_data()

        context['current_time'] = time.ctime()

        return context
    
class CreateProfileView(CreateView):
    """
        This view will display a form where the user will submit their
        Profile and it'll be saved to the database.   
        (1) display the HTML form to user (GET)
        (2) process the form submission and store the new Profile object (POST) 
    """

    # Retrieves a CreateProfileForm class
    form_class = CreateProfileForm

    # Find the template to create profile
    template_name = 'mini_fb/create_profile_form.html'

    # Get the current time for footer
    def get_context_data(self, **kwargs):
        context = super().get_context_data()

        context['current_time'] = time.ctime()

        return context