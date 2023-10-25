from django.urls import path
from home import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.index,name='index' ),

    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name="login"),
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),
    path('register/', views.register, name="register"),
    path('accounts/profile/', views.index, name="profile"),


    path('index/',views.index,name='index' ),
    path('about/',views.about,name='about' ),
    path('price/',views.price,name='price' ),
    path('service/',views.service,name='service' ),
    path('contact/',views.contact,name='contact' ),
]
