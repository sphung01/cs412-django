# blog/models.py
# Define the data objects for our application
#
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Article(models.Model):
    '''Encapsulate the idea of an Article by some author.'''

    # data attributes of a Article:
    title = models.TextField(blank=False)
    author = models.TextField(blank=False)
    text = models.TextField(blank=False)
    published = models.DateTimeField(auto_now=True)
    # image_url = models.URLField(blank=True) ## new
    image_file = models.ImageField(blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE) ## NEW
    
    def __str__(self):
        '''Return a string representation of this Article object.'''
        return f'{self.title} by {self.author}'
    
    def get_absolute_url(self):
        '''Return the URL to display one instance of this model.'''
        return reverse('blog:article', kwargs={'pk':self.pk})
    
    def get_all_comments(self):
        '''Return all of the comments about this article.'''

        comments = Comment.objects.filter(article=self)
        return comments
    
class Comment(models.Model):
    '''Encapsulate the idea of an Article by some author.'''

    # data attributes of a Article:
    article = models.ForeignKey("Article", on_delete=models.CASCADE)
    author = models.TextField(blank=False)
    text = models.TextField(blank=False)
    published = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        '''Return a string representation of this Comment object.'''
        return f'{self.text}'
    