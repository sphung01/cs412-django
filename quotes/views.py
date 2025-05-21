# File: quotes/views.py
# Author: Steven Phung (sphung01@bu.edu), 5/20/2025
# Description: This file handles web requests for the
# 'quotes' app. Each function returns/renders a template
# along with the current time and the random quote/image
# of Albert Einstein

from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

import time
import random

"""
Contains a list of Albert Einstein's quotes
"""
quote_list = [
    "Life is like riding a bicycle. To keep your balance, you must keep moving.",
    "Look deep into nature, then you will understand everything better.",
    "Weakness attitude becomes weakness of character",
    "The only source of knowledge is experience",
    "The hardest thing to understand in the world is the income tax",
]

"""
Contains a list of Albert Einstein's images
"""
image_list = [
    "https://hips.hearstapps.com/hmg-prod/images/albert-einstein-sticks-out-his-tongue-when-asked-by-news-photo-1681316749.jpg?crop=1.00xw:0.956xh;0,0.0437xh&resize=980:*",
    "https://see-sciencecenter.org/wp-content/uploads/2022/11/Einstein.jpg",
    "https://einstein-website.de/en/wp-content/uploads/sites/3/2022/06/Einstein_MK-795x1024.jpg",
    "https://static.independent.co.uk/s3fs-public/thumbnails/image/2013/10/07/12/Einstein-brain-web.jpg",
    "https://paw.princeton.edu/sites/default/files/styles/hero_half/public/images/content/Einstein_ledeNew.jpg?h=94b2eb50&itok=UfyyS9zB",
]

def random_quote():
    """
        This function randomly chooses one quote from the 'quote_list'
        and returns that quote to display to the user.
    """
    quote = random.choice(quote_list)
    return quote

def random_image():
    """
        This function randomly chooses one image from the 'image_list'
        and returns that image to display to the user.
    """
    image = random.choice(image_list)
    return image

# Create your views here.
def home_page(request):
    '''
        Defines a view to show the 'home.html'

        Return:
            - A render function that will return the response to the user
              that contains the finalized rendered HTML:
                - The template of the 'home.html'
                - The current time
                - A randomly chosen quote
                - A randomly chosen image
    '''

    # the template to which we will delegate the work
    template = 'quotes/home.html'

    # a dict of key/value pairs, to be available for use in template
    context = {
        'current_time': time.ctime(),
        'chosen_quote': random_quote(),
        'chosen_image': random_image(),
    }

    return render(request, template, context)

def quote(request):
    '''
        Defines a view to show the 'quote.html'

        Return:
            - A render function that will return the response to the user
              that contains the finalized rendered HTML:
                - The template of the 'quote.html'
                - The current time
                - A randomly chosen quote
                - A randomly chosen image
    '''

    # the template to which we will delegate the work
    template = 'quotes/quote.html'

    # a dict of key/value pairs, to be available for use in template
    context = {
        'current_time': time.ctime(),
        'chosen_quote': random_quote(),
        'chosen_image': random_image(),
    }

    return render(request, template, context)

def about(request):
    '''
        Defines a view to show the 'about.html'

        Return:
            - A render function that will return the response to the user
              that contains the finalized rendered HTML:
                - The template of the 'about.html'
                - The current time
    '''

    # the template to which we will delegate the work
    template = 'quotes/about.html'

    # a dict of key/value pairs, to be available for use in template
    context = {
        'current_time': time.ctime(),
    }

    return render(request, template, context)

def show_all(request):
    '''
        Defines a view to show the 'show_all.html'

        Return:
            - A render function that will return the response to the user
              that contains the finalized rendered HTML:
                - The template of the 'show_all.html'
                - The current time
                - A list of quotes
                - A list of images
    '''

    # the template to which we will delegate the work
    template = 'quotes/show_all.html'

    # a dict of key/value pairs, to be available for use in template
    context = {
        'current_time': time.ctime(),
        'all_quotes': quote_list,
        'all_images': image_list,
    }

    return render(request, template, context)