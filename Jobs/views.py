from django.shortcuts import render

# Create your views here.
def job (request):
    return render (request,'job.html')
def job_details(request):
    return render (request, 'job-details.html')

def job_posts(request):
    return render (request, 'job-post.html')