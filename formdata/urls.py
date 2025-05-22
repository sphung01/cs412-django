from django.urls import path
from django.conf import settings
from . import views

app_name = 'formdata'

urlpatterns = [ 
    path(r'', views.show_form, name="show_form"),
]