from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import SignUpForm,LoginForm
from django.contrib.auth import authenticate,login,logout
from  django.contrib.auth.models import User,auth
# Create your views here.
def register(request):
    msg = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            msg = 'user created'
            return redirect('login')
        else:
            msg = 'form is not valid'
    else:
        form = SignUpForm()
    return render (request ,"registration.html",{'form': form, 'msg': msg})




def login_user(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')  
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_student:
                login(request,user)
                return redirect('/candidate/candidate-details')
            elif user is not None and user.is_employee:
                login(request,user)
                return redirect('/')
            else:
                msg= 'invalid credentials'
        else:
            msg = 'error validating form'
    return render(request, 'login.html', {'form': form, 'msg': msg})
   



def logout(request):
    auth.logout(request)
    return redirect('/')

def profile (request):
    return render (request,"profile.html" )   