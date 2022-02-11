from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

# Create your views here.
def index(request):
    products = Product.objects.all()
    return render(request, 'index.html',{'products': products})
    #return HttpResponse("<h1>Welcome to django</h1>")

def about(request):
    return HttpResponse("<h1>About Page</h1>")

def contact(request):
    return render(request, 'contact.html')
    #return HttpResponse("<h1>Contact Page</h1>")

def cart(request):
    products = Product.objects.all()
    return render(request, 'cart.html',{'products': products})