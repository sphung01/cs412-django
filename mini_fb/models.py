# File: mini_fb/models.py
# Author: Steven Phung (sphung01@bu.edu), 5/27/2025
# Description: This is where we define a structured
# stored data of the model. Then we will migrate once
# a model has been created

from django.db import models

# Create your models here.
class Profile(models.Model):
    """
        Creates attributes that a Profile model should have
    """

    # Here are the data attributes of a Profile:
    first_name = models.CharField(max_length=250, blank=False)
    last_name = models.CharField(max_length=250, blank=False)
    city = models.CharField(max_length=250, blank=False)
    email_address = models.CharField(max_length=250, blank=False)
    profile_image_url = models.URLField(blank=True)

    # On the 'admin' database, we create a string that
    # represents the Profile object

    def __str__(self):
        """
            Returns a string representation of this Profile object
        """
        return f'{self.first_name} {self.last_name}'

