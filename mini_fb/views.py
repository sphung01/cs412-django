# File: mini_fb/views.py
# Author: Steven Phung (sphung01@bu.edu), 5/27/2025
# Description: In this file, we create view functions
# to send back a response to the client. Such as
# displaying the appropriate template on the web

from django.shortcuts import render
from .models import Profile 
from .forms import CreateProfileForm, CreateStatusMessageForm
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse
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
    
class CreateStatusMessageView(CreateView):
    """
        This view will display a form where the user will submit their
        Profile and it'll be saved to the database.   
        (1) display the HTML form to user (GET)
        (2) process the form submission and store the new StatusMessage object (POST) 
    """

    # Retrieves a CreateStatusMessageForm class
    form_class = CreateStatusMessageForm

    # Find the template to create profile
    template_name = 'mini_fb/create_status_form.html'

    def get_context_data(self, **kwargs):
        '''Return the dictionary of context variables for use in the template.'''

        # Calling the superclass method
        context = super().get_context_data()

        # Find/add the profile to the context data
        # Retrieve the PK from the URL pattern
        pk = self.kwargs['pk']
        profile = Profile.objects.get(pk=pk)

        # Add this profile into the context dictionary:
        context['profile'] = profile
        return context
    
    # Get the current time for footer
    def get_context_data(self, **kwargs):
        context = super().get_context_data()

        context['current_time'] = time.ctime()

        return context
    
    def form_valid(self, form):
        '''This method handles the form submission and saves the 
        new object to the Django database.
        We need to add the foreign key (of the Profile) to the message
        object before saving it to the database.
        '''

		# Instrument our code to display form fields: 
        print(f"CreateStatusMessageView.form_valid: form.cleaned_data={form.cleaned_data}")
        
        # Retrieve the PK from the URL pattern
        pk = self.kwargs['pk']
        profile = Profile.objects.get(pk=pk)
        # Attach this profile to the comment
        form.instance.profile = profile # set the FK

        # delegate the work to the superclass method form_valid:
        return super().form_valid(form)
    
    ## show how the reverse function uses the urls.py to find the URL pattern
    def get_success_url(self):
        '''Provide a URL to redirect to after creating a new Comment.'''

        # Create and return a URL:
        # Return reverse('show_all') # not ideal; we will return to this
        # Retrieve the PK from the URL pattern
        pk = self.kwargs['pk']
        # Call reverse to generate the URL for this Profile
        return reverse('mini_fb:profile', kwargs={'pk':pk})