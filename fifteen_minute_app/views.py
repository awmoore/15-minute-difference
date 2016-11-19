from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Let's get it going")

def signupform(request):
    return HttpResponse("Let's get it going. Sign me up.")

def signupcomplete(request):
    return HttpResponse("Let's get it going. I'm all signed up.")
