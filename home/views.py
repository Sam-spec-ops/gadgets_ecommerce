from django.shortcuts import render
from django.contrib import messages


def index(request):
    """ A view to return the index page """
    messages.info(request, "This page is for educational purposes only. \
                  Database is not connected and data won't be saved.")
    return render(request, 'home/index.html')
