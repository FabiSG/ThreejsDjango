from django.shortcuts import render
from django.http import HttpResponse

from datetime import datetime

def index(request):
    now = datetime.now()

    return render(
        request,
        "index.html",  # Relative path from the 'templates' folder to the template file
        # "index.html", # Use this code for VS 2017 15.7 and earlier
        {
            'title' : "Hello Django",
            'message' : "Hello Django!",
            'content' : " on " + now.strftime("%A, %d %B, %Y at %X")
        }
    )
