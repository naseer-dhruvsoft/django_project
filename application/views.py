from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def homepage(Request):
    return render(Request,'django_app.html')
    