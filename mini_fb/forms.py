from django import forms
from .models import Profile, StatusMessage

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
        model = Profile
        fields = ['first_name', 'last_name', 'city', 'email_address', 'profile_image_url']

class CreateStatusMessageForm(forms.ModelForm):
    """
        Similar to CreateProfileForm class, a form will be created
        for a user to add comments/messages to a profile.
    """

    class Meta:

        model = StatusMessage
        fields = ['message']  # which fields from model should we use
