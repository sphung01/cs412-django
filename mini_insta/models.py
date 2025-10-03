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
    display_name = models.CharField(max_length=250, blank=True)

    # This is where a client provides a photo. It can be a PNG, JPG, or anything
    profile_image_url = models.ImageField(blank=True)

    # This is where the person gets to talk about what their account is about
    bio_text = models.TextField(blank=True)

    # The time the Profile was created
    join_date = models.DateTimeField(auto_now=True)

    # A method to return all post instances for each profile
    def get_all_posts(self):
        """
            Returns all the post instances for a given Profile
        """

        # This will allow us to get filter posts for specific profiles
        # With this, we can get the querysets of the posts
        posts = Post.objects.filter(profile=self)
        return posts

    # We use __str__ to represent an object in the model
    def __str__(self):
        """
            Returns a string representation of the Profile object.
        """

        return f'{self.username} was created at {self.join_date}'
    
class Post(models.Model):
    """
        This class create Post objects and takes in the foreign key
        of Profile.
    """

    # These are the attributes we need for Post

    # Takes in a foreign key of Profile. This is basically a Many-To-One
    # relationship since one profile is allowed to have many posts.
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    # This creates a text box for people to add captions
    # for their post
    caption = models.TextField(blank=True)

    # We have a timestamp to display the time the user posted
    timestamp = models.DateTimeField(auto_now=True)

    # A method to return all Photo instances for each Post
    def get_all_photos(self):
        """
            Returns all the photo instances for a given Post
        """

        # This will allow us to get filter photos for specific posts
        # With this, we can get the querysets of the photos
        photos = Photo.objects.filter(post=self)
        return photos

    # We use __str__ to represent an object in the model
    def __str__(self):
        """
            Returns a string representation of the Post object.
        """ 

        return f'Posted by {self.profile.username} at {self.timestamp}'
    
class Photo(models.Model):
    """
        This class create Photo objects and takes in the foreign key
        of Post.
    """

    # These are the attributes we need for Photo

    # Takes in a foreign key of Post. This is a Many-to-One since a
    # post is allowed to have more than one image
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    # This is where a client provides a photo. It can be a PNG, JPG, or anything
    # The user has to give the image to the server in order to post
    image_url = models.ImageField(blank=False)

    # We have a timestamp when the user provides photos
    timestamp = models.DateTimeField(auto_now=True)

    # We use __str__ to represent an object in the model
    def __str__(self):
        """
            Returns a string representation of the Photo object.
        """

        return f'Photo for post by {self.post.profile.username} at {self.timestamp}'