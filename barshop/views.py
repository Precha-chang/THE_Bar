from django.shortcuts import render ,redirect
from django. contrib. auth.models import User
from . import models


# Create your views here.
def homepage (request):
    return render (request,"index.html")

def about (request):
    return render (request,"about.html")

def shop (request):
    return render (request,"shop.html")

def cart (request):
    return render (request,"cart.html")