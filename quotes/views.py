from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

import time

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