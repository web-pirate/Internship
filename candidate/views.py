from django.shortcuts import render

# Create your views here.
def candidate(request):
    return render (request,'candidate.html')

def candidate_details(request):
    return render (request,"candidate-details.html") 

def create_resume(request):
    return render (request,"create-resume.html")       
