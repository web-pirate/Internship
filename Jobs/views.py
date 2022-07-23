from turtle import home
from django.shortcuts import render,redirect
from Jobs.models import companydetails, job_profile
from django.contrib import messages
# Create your views here.
def job_posted(request,companyname):

    try:

         job_postedtills=job_profile.objects.all().filter(companyname=companyname)
    except:
        messages.info(request, 'No job Posted Yet')
        return redirect("/",{messages:"messages"})
    return render (request,'job.html',{"job_postedtills":job_postedtills})
    
def job_details(request,companyname,id):
    employers_details=companydetails.objects.get(companyname=companyname)
    job_details_posted=job_profile.objects.get(companyname=companyname,id=id)
    param={
        "job_details_posted":job_details_posted,
        "employers_details": employers_details
    }
    return render (request, 'job-details.html',param)

def job_posts(request):
    if request.method=="POST":
        joblogo=request.POST.get("joblogo")
        jobtitle=request.POST.get("jobtitle")
        jobcategory=request.POST.get("jobcategory")
        companyname=request.POST.get("companyname")
        location=request.POST.get("location")
        jobtags=request.POST.get("jobtags")
        salary=request.POST.get("salary")
        experience=request.POST.get("experience")
        jobdescription=request.POST.get("jobdescription")
        responsibilities=request.POST.get("responsibilities")
        requirements=request.POST.get("requirements")
        benefits=request.POST.get("benefits")

        job_post=job_profile(joblogo=joblogo,jobtitle=jobtitle,jobcategory=jobcategory,companyname=companyname,location=location,jobtags=jobtags,salary=salary,experience=experience,jobdescription=jobdescription,responsibilities=responsibilities,benefits=benefits,requirements=requirements)
        job_post.save()
        print("save")
        return redirect('/')


    return render (request, 'job-post.html')



def company_details(request):
    if request.method=="POST":
        logo=request.POST.get("logo")
        companyname=request.POST.get("companyname")
        companysize=request.POST.get("companysize")
        companyaddress=request.POST.get("companyaddress")
        companyphone=request.POST.get("companyphone")
        companyemail=request.POST.get("companyemail")
        companywebsite=request.POST.get("companywebsite")
        aboutcompany=request.POST.get("aboutcompany")
        
        if companydetails.objects.filter(companyname=companyname).exists():
            messages.info(request,'already taken')
            return redirect('/')
        elif companydetails.objects.filter(companyemail=companyemail).exists():
            messages.info(request,'email already taken')
            return redirect('/')
        else:
            companyprofile=companydetails(logo=logo,companyname=companyname,companysize=companysize,companyaddress=companyaddress,companyphone=companyphone,companyemail=companyemail,companywebsite=companywebsite,aboutcompany=aboutcompany)               
            companyprofile.save()
            return redirect(f'/jobs/employerdetails/{companyprofile.companyname}/')
    else:
        return render (request,'companydetails.html')




def employersdetails(request, companyname):  
    
    job_postedtills=job_profile.objects.all().filter(companyname=companyname)
    employers_details=companydetails.objects.get(companyname=companyname)
    params={
        "employers_details": employers_details,
        "job_postedtills":job_postedtills,
      
    } 
    return render (request,"employers-details.html",params)