from django.shortcuts import render,redirect

def home(request):
    return render (request, 'index.html')
def about(request):
    return render (request, 'aboutus.html')
def contact(request):
    return render (request, 'contact.html')
       