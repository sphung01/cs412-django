# File: mini_fb/views.py
# Author: Steven Phung (sphung01@bu.edu), 5/27/2025
# Description: In this file, we create view functions
# to send back a response to the client. Such as
# displaying the appropriate template on the web

from django.shortcuts import render
from .models import * 
from .forms import * 
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View
from django.urls import reverse
from django.shortcuts import redirect
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
        """
            Passes over one OR multiple contexts to the HTML template
        """
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
        """
            Passes over one OR multiple contexts to the HTML template
        """
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
        """
            Passes over one OR multiple contexts to the HTML template
        """
        context = super().get_context_data(**kwargs)

        pk = self.kwargs['pk']
        profile = Profile.objects.get(pk=pk)

        context['profile'] = profile
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

        # Save the status message to database
        sm = form.save()

        # Read the file from the form:
        files = self.request.FILES.getlist('files')
        caption = self.request.POST.get('caption')

        # Now we will loop through the files
        # since we assume there may bee more than one image file.
        # This is to create Image and StatusImage objects.
        for file in files:
            img = Image(profile=sm.profile, image_file=file, caption=caption) # Creates Image object
            img.save() # Saves this Image object to the database

            status_img = StatusImage(status_message=sm, image=img) # Creates StatusImage object
            status_img.save() # Saves this StatusImage object to the database

        # delegate the work to the superclass method form_valid:
        return super().form_valid(form)
    
class UpdateProfileView(UpdateView):
    """
        This will allow a user to update the Profile with
        the use of the PUT operation.
    """

    # Retrieves the Profile model
    model = Profile

    # Retrieves the UpdateProfileForm class
    form_class = UpdateProfileForm

    # Find the template to update the Profile object
    template_name = 'mini_fb/update_profile_form.html'

    def get_context_data(self, **kwargs):
        """
            Passes over one OR multiple contexts to the HTML template
        """
        context = super().get_context_data()

        context['current_time'] = time.ctime()

        return context

class DeleteStatusMessageView(DeleteView):
    """
        This will allow the user to delete the Message instance and
        the server will remove from the database
    """

    # Retrieves the StatusMessage model
    model = StatusMessage

    # Find the template to delete the StatusMessage object
    template_name = 'mini_fb/delete_status_form.html'

    # Passes over the context to HTML
    context_object_name = 'message'

    def get_success_url(self):
        """
            Redirects user to a Profile page after
            deleting the message.
        """
        return reverse('mini_fb:profile', kwargs={'pk': self.object.profile.pk})
    
    def get_context_data(self, **kwargs):
        """
            Passes over one OR multiple contexts to the HTML template
        """
        context = super().get_context_data()

        context['current_time'] = time.ctime()

        return context

class UpdateStatusMessageView(UpdateView):
    """
        This will allow the user to update the Message instance and
        the server will remove from the database
    """

    # Retrieves the StatusMessage model
    model = StatusMessage

    # Retrieves the UpdateMessageForm
    form_class = UpdateMessageForm

    # Passes over the context to HTML
    context_object_name = 'status'

    # Find the template to update the StatusMessage object
    template_name = 'mini_fb/update_status_form.html'

    def get_context_data(self, **kwargs):
        """
            Passes over one OR multiple contexts to the HTML template
        """
        context = super().get_context_data()

        context['current_time'] = time.ctime()

        return context

class AddFriendView(View):
    """
        Creates a view when adding a friend on a specific Profile instance.
        We will need to call the add friends method.
    """

    def dispatch(self, request, *args, **kwargs):
        """
            This will allow us to get the parameters from the
            URL such as 'pk' (Profile we are looking into) and
            'other_pk' (A Profile we are adding as a friend).
        """

        # We get the parameters of the URL
        profile_id = kwargs.get('pk')
        other_id = kwargs.get('other_pk')

        # Use the keys to get the Profile objects
        profile = Profile.objects.get(pk=profile_id)
        other_profile = Profile.objects.get(pk=other_id)

        # Then the profile we are looking into will add the other as friend
        profile.add_friend(other_profile)

        # We provide the HTTP response back to the user after adding
        return redirect('mini_fb:profile', pk=profile_id)
    
class ShowFriendSuggestionsView(DetailView):
    """
        Displays a page that shows all of the profiles
        suggested to be friends with.
    """

    # Retriving the Profile model
    model = Profile

    # Finding the HTML to friend suggestions
    template_name = 'mini_fb/friend_suggestion.html'

    # Pass the context to the HTML
    context_object_name = 'profile'

    def get_context_data(self, **kwargs):
        """
            Passes over one OR multiple contexts to the HTML template
        """
        context = super().get_context_data()

        context['current_time'] = time.ctime()

        return context
    
class ShowNewsFeedView(DetailView):
    """
        This will display all of the status messages
        from the profile itself and friends.
    """

    # We are using the Profile model to get the list of all the messages
    model = Profile

    # Find the template to display news feed
    template_name = 'mini_fb/news_feed.html'

    context_object_name = 'profile'

    def get_context_data(self, **kwargs):
        """
            Passes over one OR multiple contexts to the HTML template
        """
        context = super().get_context_data()

        context['current_time'] = time.ctime()

        return context