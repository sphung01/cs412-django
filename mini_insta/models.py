from django.db import models

# Create your models here.
class Profile(models.Model):
    """
        Creates attributes that a Profile model should have.
    """

    # These are the attributes of in the Profile model

    # We create a username for the Profile
    username = models.CharField(max_length=250, blank=False)

    # Normally, Instagram allows people to display their names
    display_name = models.CharField(max_length=250, blank=False)

    # This is where a client provides a photo. It can be a PNG, JPG, or anything
    profile_image_url = models.ImageField(blank=True)

    # This is where the person gets to talk about what their account is about
    bio_text = models.TextField(blank=False)

    # The time the Profile was created
    join_date = models.DateTimeField(auto_now=True)

    # We use __str__ to represent an object in the model
    def __str__(self):
        """
            Returns a string representation of the Profile object.
        """

        return f'{self.username} was created at {self.join_date}'