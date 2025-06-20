from django.shortcuts import render

# Create your views here.
def home(request):

    template = 'project/home.html'

    return render(request, template)
