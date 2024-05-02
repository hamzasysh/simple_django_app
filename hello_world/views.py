from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# simple_django_app/hello_world/views.py


def hello_world(request):
    return HttpResponse("Hello, World!")
