from django.shortcuts import render,redirect
from django.db import IntegrityError
from django.contrib.auth.models import User
from django.contrib import admin


def index(request):
    if request.user.is_authenticated:
        return render(request, 'index.html') 
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')

def service(request):
    return render(request, 'service.html')

def price(request):
    return render(request, 'price.html')

def contact(request):
    return render(request, 'contact.html')

def register(request):
    if request.method == "POST":
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        email = request.POST.get("email")
        username = request.POST.get("username")
        password = request.POST.get("password")

        try:

            new_user = User.objects.create_user(username, email, password)
            # new_user = UserCreationForm(request.POST)
            new_user.first_name = fname
            new_user.last_name = lname

            new_user.save()
            return redirect("login")
            # Redirect or perform other actions for successful registration
        except IntegrityError:
            # Handle the case when a user with the same username already exists
            error_message = (
                "Username already exists. Please choose a different username."
            )
            return render(
                request,
                "register.html",
                {"error_message": error_message},
            )

    else:
        return render(
            request, "register.html"
        ) 
# Create your views here.
