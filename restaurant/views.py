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
