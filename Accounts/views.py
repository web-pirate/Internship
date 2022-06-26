
from django.shortcuts import render,redirect

# Create your views here.
def register(request):
    return render (request ,"registration.html")

def login(request):
    return render (request ,"login.html")



def logout(request):
    return render (request ,"home.html")

def profile (request):
    return render (request,"profile.html" )   