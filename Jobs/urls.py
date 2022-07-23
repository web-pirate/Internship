from django.contrib import admin
from django.urls import path,include
from django.urls.conf import include
from . import views

urlpatterns = [
    path("job-posted/<companyname>", views.job_posted, name="job-posted"),
    path("job-details/<companyname>/<id>/", views.job_details, name="job-details"),
    path("job-posts", views.job_posts, name="job-posts"),
    path("employersdetails/<companyname>/",views.employersdetails,name="employersdetails"),
    path("company-details/",views.company_details,name="company-details")
   
]