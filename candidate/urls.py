from django.contrib import admin
from django.urls import path,include
from django.urls.conf import include
from . import views

urlpatterns = [
    path("candidate", views.candidate, name="candidate"),
    path("candidate-details",views.candidate_details,name="candidate_details"),
    path("create-resume",views.create_resume,name="create_resume"),
    
   
]