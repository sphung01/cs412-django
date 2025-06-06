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
    profile_image_file = models.ImageField(blank=True)

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
    
    def get_friends(self):
        """
            Returns the list of Friends other than the profile itself.
        """

        # This checks which Friend instance has the Profile object we
        # are looking into. For example, we look to see if Gumball
        # is in one of these instances by filtering. Whether he is
        # profile1 or profile2.
        friends = Friend.objects.filter(profile1=self) | Friend.objects.filter(profile2=self)

        # We make an empty list 'profile_friends'
        profile_friends = []

        # For every friend we are checking...
        for friend in friends:
            # If this Profile model is profile1,
            # we append the other one that is not this profile instance.
            if friend.profile1 == self:
                profile_friends.append(friend.profile2)
            # Otherwise just append profile1
            else:
                profile_friends.append(friend.profile1)

        # With that, we return the list of friends for this Profile instance.
        return profile_friends

    def add_friend(self, other):
        """
            This helps create a Friend instance if two profiles
            are not friends (self and other).
        """

        # Check if they are not friending themselves
        if self != other:
            # Check if the friendship already exists
            existing_friends1 = Friend.objects.filter(profile1=self, profile2=other)
            existing_friends2 = Friend.objects.filter(profile1=other, profile2=self)

            # Only add the friend if no such record exists
            if not existing_friends1.exists() and not existing_friends2.exists():
                print('They became friends!')
                new_friend = Friend(profile1=self, profile2=other)
                new_friend.save()
            else:
                print('Already friends')
                return
        else:
            print('Cannot friend yourself')
            return
    
    def get_friend_suggestions(self):
        """
            This will return the list of Profiles that are not
            friends with this instance.
        """ 

        # We will collect all profiles that exist
        all_profiles = Profile.objects.all()

        # Get list of Profiles that are friends with this instance
        friends = self.get_friends()

        # Create empty suggestion list
        suggestion_list = []

        # For every profile that exists
        for profile in all_profiles:
            # If the Profile is not in the friends list and not the profile we are looking at
            if profile not in friends and profile != self:
                # Add that Profile to the suggestion list
                suggestion_list.append(profile)
        
        # Return the suggestion list
        return suggestion_list

    def get_news_feed(self):
        """
            This will return the list of all StatusMessages of this
            Profile object and Friends.
        """

        # We will create empty list that will hold
        # friend Profiles and our own Profile (self).
        profiles = []

        # Then start appending.
        for friend in self.get_friends():
            profiles.append(friend)
        profiles.append(self)

        # We can filter by checking each profile in 'profiles' list.
        # __in is a ORM Lookup that checks there is a value in the list.
        # order_by allows us to sort the list during filter.
        # With '-timestamp', this helps sort the messages from newest to oldest.
        news_feed_list = StatusMessage.objects.filter(profile__in=profiles).order_by('-timestamp')

        return news_feed_list       

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
    
    def get_absolute_url(self):
        """
            Return the URL to display one instance of this model.
        """
        return reverse('mini_fb:profile', kwargs={'pk':self.profile.pk})
    
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

class Friend(models.Model):
    """
        Encapsulates an idea of connecting two nodes within the
        social network. For example, connecting two friends together.
    """

    # Here are the fields/attributes
    profile1 = models.ForeignKey(Profile, related_name="profile1", on_delete=models.CASCADE)
    profile2 = models.ForeignKey(Profile, related_name="profile2", on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        """
            Returns a string representation of the Friend model
        """

        return f'{self.profile1.first_name} {self.profile1.last_name} & {self.profile2.first_name} {self.profile2.last_name}'