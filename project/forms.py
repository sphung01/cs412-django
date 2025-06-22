from django import forms
from .models import *

class CreateUserForm(forms.ModelForm):
    """
        Adds a new user to the database
    """

    class Meta:
        '''associate this form with a model from our database.'''
        model = ProjectUser
        fields = ['first_name', 'last_name', 'email', 'role', 'student_id', 'profile_image']