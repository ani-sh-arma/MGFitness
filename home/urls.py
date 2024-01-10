from django.urls import path
from home import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView
from django.contrib import admin

urlpatterns = [

    
    path('',views.index,name='index' ),

    path('login/', LoginView.as_view(template_name='login.html'), name="login"),
    path('logout/', auth_views.LogoutView.as_view(template_name="login.html"), name="logout"),
    path('register/', views.register, name="register"),
    path('profile/', views.profile, name="profile"),
    path('profile/update_profile', views.update_profile, name="update_profile"),


    path('index/',views.index,name='index' ),
    path('about/',views.about,name='about' ),
    path('price/',views.price,name='price' ),

    path('thanks/',views.thanks,name='thanks' ),
    path('contact/',views.contact,name='contact' ),

    path('contact/contact_mail/' , views.contact_mail , name="contact_mail")

]
