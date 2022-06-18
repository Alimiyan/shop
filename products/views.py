from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product
from .forms import NewUserForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
# a function to check if user is logged in
def check_loggedin(request):
    if request.user.is_authenticated:
        return render(request, 'index.html')
    else:
        return redirect('/login')


def index(request):
    products = Product.objects.all()
    if request.user.is_authenticated:
        print("User is logged in :)")
        print(f"Username --> {request.user.username}")
    else:
        print("User is not logged in")
    return render(request, 'index.html', {'products': products})
    # return HttpResponse("<h1>Welcome to django</h1>")


def about(request):
    return HttpResponse("<h1>About Page</h1>")


def contact(request):
    return render(request, 'contact.html')
    # return HttpResponse("<h1>Contact Page</h1>")

@login_required
def cart(request):
    products = Product.objects.all()
    return render(request, 'cart.html', {'products': products})


def register(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        print(form.errors)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"New account created: {username}")
            return redirect('/')
        else:
            messages.error(request, "Invalid username or password.")
            return HttpResponse("<h1>Error in Registration</h1>")
    form = NewUserForm()
    return render(request, 'register.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect('/')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout(request):
    auth_logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect('/')