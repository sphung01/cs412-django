# File: mini_fb/forms.py
# Author: Steven Phung (sphung01@bu.edu), 5/29/2025
# Description: In this file, we create forms where they
# handle user input and pass it over to the database
# through Django's ModelForm.

from django import forms
from .models import Profile, StatusMessage

# Created a CreateProfileForm class
class CreateProfileForm(forms.ModelForm):
    """
        When a form is submitted, a new Profile object will
        be created and then sent to the database.
    """

    first_name = forms.CharField(label="First Name", required=True)
    last_name = forms.CharField(label="Last name", required=True)


    class Meta:
        """
            Associates this form with a model from database.
        """

        # Focuses on a specific model
        model = Profile

        # Which fields from model should we use
        fields = ['first_name', 'last_name', 'city', 'email_address', 'profile_image_file']

# Created a CreateStatusMessageForm class
class CreateStatusMessageForm(forms.ModelForm):
    """
        Similar to CreateProfileForm class, a form will be created
        for a user to add comments/messages to a profile.
    """

    class Meta:

        # Focuses on a specific model
        model = StatusMessage

        # Which fields from model should we use
        fields = ['message']

class UpdateProfileForm(forms.ModelForm):
    """
        This class will have a form where we can
        update a Profile object.
    """

    class Meta:
        """
            Associates this form with the Profile model.
        """

        # Focuses on the Profile model
        model = Profile

        # Fields that we should use from the Profile model
        fields = ['city', 'email_address', 'profile_image_file']

