from django.shortcuts import render


# Create your views here.
def homepage(Request):
    return render(Request,'django_app.html')
    