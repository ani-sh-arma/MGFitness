from .models import member
from django.shortcuts import render,redirect
from django.db import IntegrityError
from django.contrib.auth.models import User
from django.contrib import admin
from .forms import UserProfileForm
from django.conf import settings
import stripe

from django.urls import reverse

from .models import member

from .utils import send_email_to_client


def index(request):
    if request.user.is_authenticated:
        return render(request, 'index.html',{'user':request.user}) 


    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        msg = request.POST.get("message")

        subject = "An email from " + " "+name
        message = f"{msg}\n\n Email : {email} \n Phone No : {phone}"
        recipient_list = ['anisharma030@gmail.com']

        send_email_to_client(subject , message , recipient_list)

        return redirect(" ")

    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def thanks(request):
    return render(request, 'service.html')


def update_profile(request):
    current_user_member = member.get_current_user(request.user)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=current_user_member)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Change 'profile' to the actual URL name of your profile page
    else:
        form = UserProfileForm(instance=current_user_member)

    return render(request, 'update_profile.html', {'form': form})




from django.shortcuts import render
from .models import member

def profile(request):
    if request.user.is_authenticated:
        # Use the get_current_user method to fetch the user's data
        current_user_data = member.get_current_user(request.user)
        is_member = current_user_data is not None

        # Check if the user data exists
        if current_user_data:
            return render(request, 'profile.html', {'user': request.user, 'userData': current_user_data , 'is_member': is_member})

    return render(request, 'profile.html')


def price(request):

    stripe.api_key = settings.STRIPE_SECRET_KEY

    checkout_session = stripe.checkout.Session.create(
        line_items=[
            {
                # Provide the exact Price ID (for example, pr_1234) of the product you want to sell
                'price': 'price_1OLPEASF5zr91hwvpzmLQqDg',
                'quantity': 1,
            },
        ],
        mode='payment',
        success_url=request.build_absolute_uri(reverse("thanks")) + '?session_id={CHECKOUT_SESSION_ID}',
        cancel_url= request.build_absolute_uri(reverse("price")),
    )
    
    context = {
    'session_id': checkout_session['id'],
    'stripe_publishable_key': settings.STRIPE_PUBLISHABLE_KEY
}





    return render(request, 'price.html', context)



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
    
def contact_mail(request):
    
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        msg = request.POST.get("message")

        subject = "An email from " + " "+name
        message = f"{msg}\n\n Email : {email} \n Phone No : {phone}"
        recipient_list = ['22amtics405@gmail.com']

        for i in range(5):
            
            send_email_to_client(subject , message , recipient_list)

        return redirect("contact")
    
    return render(request,'contact.html')
