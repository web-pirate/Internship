from django.contrib import admin
from django.urls import path,include
from django.urls.conf import include
from . import views

urlpatterns = [
    path("register", views.register, name="register"),
    path("login",views.login_user,name="login"),
    path("logout",views.logout,name="logout"),
    path("profile",views.profile,name="profile")
    
   
]