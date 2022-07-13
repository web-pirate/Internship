from django.shortcuts import render,redirect
from Jobs.models import job_profile
from django.db.models import Count



def home(request):
    myposts=job_profile.objects.all()
    params={
       "myposts": myposts
    }
    return render (request, 'index.html',params)
def about(request):
    return render (request, 'aboutus.html')
def contact(request):
    return render (request, 'contact.html')
       