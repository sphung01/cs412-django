from django.db import models
from django.urls import reverse

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

        posts = Post.objects.filter(profile=self)
        return posts
    
    def get_followers(self):
        followers = Follow.objects.filter(profile=self)

        profile_followers = []

        for follower in followers:

            profile_followers.append(follower.follower_profile)

        
        return profile_followers
    
    def get_num_followers(self):

        return len(self.get_followers())
    
    def get_following(self):
        following = Follow.objects.filter(follower_profile=self)
        profiles_following = [f.profile for f in following]
        return profiles_following
    
    def get_num_following(self):
        return len(self.get_following())
    
    def get_absolute_url(self):
        return reverse('mini_insta:show_profile', kwargs={'pk':self.pk})

    # We use __str__ to represent an object in the model
    def __str__(self):
        """
            Returns a string representation of the Profile object.
        """

        return f'{self.username} was created at {self.join_date}'
    
class Follow(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="profile")
    follower_profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="follower_profile")
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.follower_profile.username} followed {self.profile.username} at {self.timestamp}'

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
    
    def get_all_comments(self):
        comments = Comment.objects.filter(post=self)
        return comments
    
    def get_likes(self):
        likes = Like.objects.filter(post=self)
        return likes

    # We use __str__ to represent an object in the model
    def __str__(self):
        """
            Returns a string representation of the Post object.
        """ 

        return f'Posted by {self.profile.username} at {self.timestamp}'

    def get_absolute_url(self):
        """
            Return the URL to display one instance of this model.
        """
        return reverse('mini_insta:show_post', kwargs={'pk': self.pk})
    
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
    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now=True)
    text = models.TextField(blank=False)

    def __str__(self):
        return f'Comment: "{self.text}" by {self.profile.username} at {self.timestamp}'
    
class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.post} liked by {self.profile.username} at {self.timestamp}'