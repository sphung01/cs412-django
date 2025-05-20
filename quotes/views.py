from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

import time
import random

quote_list = [
    "Life is like riding a bicycle. To keep your balance, you must keep moving.",
    "Look deep into nature, then you will understand everything better.",
    "Weakness attitude becomes weakness of character",
    "The only source of knowledge is experience",
    "The hardest thing to understand in the world is the income tax",
]

image_list = [
    "https://hips.hearstapps.com/hmg-prod/images/albert-einstein-sticks-out-his-tongue-when-asked-by-news-photo-1681316749.jpg?crop=1.00xw:0.956xh;0,0.0437xh&resize=980:*",
    "https://see-sciencecenter.org/wp-content/uploads/2022/11/Einstein.jpg",
    "https://einstein-website.de/en/wp-content/uploads/sites/3/2022/06/Einstein_MK-795x1024.jpg",
    "https://static.independent.co.uk/s3fs-public/thumbnails/image/2013/10/07/12/Einstein-brain-web.jpg",
    "https://paw.princeton.edu/sites/default/files/styles/hero_half/public/images/content/Einstein_ledeNew.jpg?h=94b2eb50&itok=UfyyS9zB",
]

# Create your views here.
def home_page(request):
    '''
        Defines a view to show the 'home.html'
    '''

    # the template to which we will delegate the work
    template = 'quotes/home.html'

    # a dict of key/value pairs, to be available for use in template
    context = {
        'current_time': time.ctime(),
    }

    return render(request, template, context)

def quote(request):
    '''
        Defines a view to show the 'quote.html'
    '''

    # the template to which we will delegate the work
    template = 'quotes/quote.html'

    # a dict of key/value pairs, to be available for use in template
    context = {
        'current_time': time.ctime(),
    }

    return render(request, template, context)

def about(request):
    '''
        Defines a view to show the 'about.html'
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
    '''

    # the template to which we will delegate the work
    template = 'quotes/show_all.html'

    # a dict of key/value pairs, to be available for use in template
    context = {
        'current_time': time.ctime(),
    }

    return render(request, template, context)