from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def homepage(Request):
    return HttpResponse("Hello World! I am a Django application created by Naseer. This application is now enabled with auto deployments")
