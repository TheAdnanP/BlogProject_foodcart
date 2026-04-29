from .models import Product                                                                                              
from django.shortcuts import redirect, render

# Create your views here.

def home(request):
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")

def contact(request):
    return render(request,"contact.html")

def cookies(request):
    return render(request,"cookies.html")

def testimonial(request):
    return render(request,"testimonial.html")