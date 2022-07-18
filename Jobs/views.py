from turtle import home
from django.shortcuts import render,redirect
from Jobs.models import job_profile

# Create your views here.
def job_posted(request,companyname):
    job_postedtill=job_profile.objects.get(companyname=companyname)
    params={
        "job_postedtill":job_postedtill
    }

    return render (request,'job.html',params)
    
def job_details(request,companyname,id):
    job_details_posted=job_profile.objects.get(companyname=companyname,id=id)
    param={
        "job_details_posted":job_details_posted
    }
    return render (request, 'job-details.html',param)

def job_posts(request):
    if request.method=="POST":
        jobtitle=request.POST.get("jobtitle")
        jobcategory=request.POST.get("jobcategory")
        companyname=request.POST.get("companyname")
        companymail=request.POST.get("companymail")
        location=request.POST.get("location")
        jobtags=request.POST.get("jobtags")
        salary=request.POST.get("salary")
        experience=request.POST.get("experience")
        aboutcompany=request.POST.get("aboutcompany")
        jobdescription=request.POST.get("jobdescription")
        
        job_post=job_profile(jobtitle=jobtitle,jobcategory=jobcategory,companyname=companyname,companymail=companymail,location=location,jobtags=jobtags,salary=salary,experience=experience,aboutcompany=aboutcompany,jobdescription=jobdescription)
        job_post.save()
        print("save")
        return redirect('/')


    return render (request, 'job-post.html')