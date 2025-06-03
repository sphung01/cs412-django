# File: mini_fb/models.py
# Author: Steven Phung (sphung01@bu.edu), 5/27/2025
# Description: This is where we define a structured
# stored data of the model. Then we will migrate once
# a model has been created

from django.db import models
from django.urls import reverse

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
    
    def get_status_message(self):
        """
            Returns all comments on a specific Profile
        """
        messages = StatusMessage.objects.filter(profile=self)
        return messages
    
    def get_absolute_url(self):
        """
            Return the URL to display one instance of this model.
        """
        return reverse('mini_fb:profile', kwargs={'pk':self.pk})
    
class StatusMessage(models.Model):
    """
        Creates attributes that a Comment object should have.
        The comments will also connect to a specific
        profile we are looking into.
    """

    # Here are the attributes of the Comment object
    timestamp = models.DateTimeField(auto_now=True)
    message = models.TextField(blank=False)
    profile = models.ForeignKey("Profile", on_delete=models.CASCADE)

    def __str__(self):
        """
            Returns a string representation of the Comment object.
        """
        return f'{self.message} (Sent at {self.timestamp})'
    
    def get_images(self):
        images = Image.objects.filter(statusimage__status_message=self)
        return images
    
class Image(models.Model):
    """
        Represents an image uploaded by a user and associated with their profile.
    """

    # Here are the attributes of the Image object
    profile = models.ForeignKey("Profile", on_delete=models.CASCADE)
    image_file = models.ImageField(blank=True)
    timestamp = models.DateTimeField(auto_now=True)
    caption = models.TextField(blank=True)

    def __str__(self):
        """
            Returns a string representation of the Comment object.
        """
        return f'{self.image_file} (Caption: {self.caption})'

class StatusImage(models.Model):
    """
        Links a status message to an image, allowing images to be attached to posts.
    """

    # Here are the attributes of the StatusImage object
    status_message = models.ForeignKey("StatusMessage", on_delete=models.CASCADE)
    image = models.ForeignKey("Image", on_delete=models.CASCADE)


