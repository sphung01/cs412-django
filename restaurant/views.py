# File: restaurant/views.py
# Author: Steven Phung (sphung01@bu.edu), 5/22/2025
# Description: This file handles web requests from clients for the
# 'restaurant' app. Then returns a response to the user.

from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

import time
import random

# A list of special items to put on the menu
daily_special_list = [
    "Krabby Kelp Pelt",
    "Bubble Bass Burrito",
    "Cheddar Coral Crunch",
    "Deep Sea Deluxe",
    "Neptune's Feast",
]

# This will keep track of the orders that the client gave
order_list = []

def get_daily_special():
    """
        This function will randomize the 'daily_special_list'
        and return one special item to the menu.
    """

    # Randomizes a special_item
    special_item = random.choice(daily_special_list)

    return special_item

def get_ready_time():
    """
        This function will calculate the expected 'ready time'
        and then returns it
    """

    # Gets the start time (in seconds).
    start_time = time.time()

    # Randomly generate a random integer for minutes
    # Then multiply minutes by 60 seconds.
    minutes = random.randint(30, 60)
    minutes_to_seconds = minutes * 60

    # Adds the time it takes to get the order ready
    # to the start_time.
    progress_time = start_time + minutes_to_seconds

    # We will then convert the 'progress_time' (seconds)
    # to an actual time.
    ready_time = time.ctime(progress_time)

    return ready_time

def main(request):
    """
        Defines a view for the 'main.html'

        Args:
            - request: A request given to the server from the client

        Return:
            Renders the request and template for the client and returns a response
    """

    # Stores the path of the HTML template for rendering
    template = 'restaurant/main.html'

    context = {
        'mr_krabs_image': "https://static.wikia.nocookie.net/spongebob/images/7/7b/Krabs_artwork.png/revision/latest?cb=20220807045807",
        'current_time': time.ctime(),
    }

    return render(request, template, context) 

def order(request):
    """
        Defines a view for the 'order.html'

        Args:
            - request: A request given to the server from the client

        Return:
            Renders the request, template and context and returns a response
    """

    # Stores the path of the HTML template for rendering
    template = 'restaurant/order.html'

    context = {
        'daily_special_item': get_daily_special()
    }

    return render(request, template, context)

def confirmation(request):
    """
        Defines a view for the 'confirmation.html'

        Args:
            - request: A request given to the server from the client

        Return:
            Renders the request and template for the client and returns a response
    """

    # Stores the path of the HTML template for rendering
    template = 'restaurant/confirmation.html'

    # read the form data into python variables:
    if request.POST:

        name = request.POST['name']

        context = {
            'name': name,
            'expected_time': get_ready_time(),
        }

    return render(request, template, context)
