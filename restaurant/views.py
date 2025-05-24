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
    ready_time = time.strftime("%H:%M:%S %p", time.localtime(progress_time))

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
        'daily_special_item': get_daily_special(), # Calls for the random daily item
        'current_time': time.ctime(),
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

        # Initializing the lists and total_cost of the order.

        # Both combo_items and side_items create a list on inputs
        # that have the same name, either 'combo', 'topping', or 'side', 
        # by using request.POST.getlist().
        combo_items = request.POST.getlist('combo') 
        topping_items = request.POST.getlist('topping')
        side_items = request.POST.getlist('side')

        # We will for loop and add the price to the total
        total_cost = 0 

        # This list will hold all the chosen items from the client
        chosen_items = []

        # For every item in the 'combo_items' list...
        for item in combo_items:

            # First, split the string into (name of item) | (price of item)
            name, price = item.split('|') # e.g Krabby Patty|2.00

            # Second, convert the string of the price into a float value
            item_price = float(price)

            # Third, add the price to the total
            total_cost += item_price

            # Lastly, append the name of the item to the 'chosen_items' list.
            # Then, repeat process with other items
            chosen_items.append(name)

        # Just like the 'combo_items' for loop, it is the same concept
        for appetizer in side_items:
            name, price = appetizer.split('|')
            appetizer_price = float(price)
            total_cost += appetizer_price
            chosen_items.append(name)

        # Just like the 'combo_items' and 'side_items' for loop, it is the same concept
        for topping in topping_items:
            name, price = topping.split('|')
            topping_price = float(price)
            total_cost += topping_price
            chosen_items.append(name)

        # We use request.POST.get() to avoid the error.
        # Will return 'None' if the client did not check
        # the daily item. Otherwise...
        chosen_daily_item = request.POST.get('daily_item')

        # If the client DID check for daily item
        # We run the splitting name and price procedure
        # just like 'side_items' and 'combo_items'
        if chosen_daily_item:
            name, price = chosen_daily_item.split('|')
            chosen_daily_item_price = float(price)
            total_cost += chosen_daily_item_price
            chosen_items.append(name)

        # Special Instructions given from the client
        special_instructions = request.POST['special_instructions']

        # Information given from the client
        name = request.POST['name']
        email = request.POST['email']
        phone_number = request.POST['phone_number']

        context = {
            'name': name,
            'email': email,
            'phone_number': phone_number,
            'expected_time': get_ready_time(),
            'total_cost': f"{total_cost:.2f}",
            'chosen_items': chosen_items,
            'special_instructions': special_instructions,
            'current_time': time.ctime(),
        }

    return render(request, template, context)
