from django.contrib import admin
from django.urls import path,include
from django.urls.conf import include
from . import views

urlpatterns = [
    path("job", views.job, name="job"),
    path("job-details", views.job_details, name="job-details"),
    path("job-posts", views.job_posts, name="job-posts"),
    
    
   
]