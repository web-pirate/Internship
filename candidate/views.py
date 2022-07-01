from django.shortcuts import redirect, render

from  django.contrib.auth.models import User
from candidate.models import student_details

# Create your views here.


def candidate_details(request,username):
    details=student_details.objects.get(username=username)
    params={
        "details":details
    }
    

    return render (request,"candidate-details.html",params) 

def create_resume(request):
    if request.method=="POST":
       username=request.POST.get("username")
       profile_image=request.POST.get("profile_image")
       name=request.POST.get("name")
       middlename=request.POST.get("middlename")
       lastname=request.POST.get("lastname")
       dob=request.POST.get("dob")
       city=request.POST.get("city")
       state=request.POST.get("state")
       country=request.POST.get("country")
       pnumber=request.POST.get("pnumber")
       email=request.POST.get("email")
       address=request.POST.get("address")
       graduation=request.POST.get("graduation")
       college=request.POST.get("college")
       degree=request.POST.get("degree")
       additionalinformation=request.POST.get("additionalinformation")
       companyname=request.POST.get("companyname")
       jobposition=request.POST.get("jobposition")
       location=request.POST.get("location")
       DateFrom=request.POST.get("DateFrom")
       DateTo=request.POST.get("DateTo")
       additionalInformation2=request.POST.get("additionalInformation2")
       skills=request.POST.get("skills")
       skillsproficiency=request.POST.get("skillsproficiency")
       
       profile=student_details(username=username,profile_image=profile_image,name=name,middlename=middlename,lastname=lastname,dob=dob,city=city,state=state,country=country,pnumber=pnumber,email=email,address=address,graduation=graduation,college=college,degree=degree,additionalinformation=additionalinformation,companyname=companyname,jobposition=jobposition,location=location,DateFrom=DateFrom,DateTo=DateTo,additionalInformation2=additionalInformation2,skills=skills,skillsproficiency=skillsproficiency)
       profile.save()
       print("resume save")
       return redirect(f'/candidate/candidate-details/{profile.username}')

       
    return render (request,"create-resume.html")       
