from email.utils import localtime
from turtle import title
from typing_extensions import Self
import uuid
from  django.contrib.auth.models import User
from django.db import models
from django.forms import IntegerField
from pkg_resources import Requirement


job_type={
        ("full-time","full-time"),
        ("part-time","part-time"),
    }
# Create your models here.
class job_profile(models.Model):
    id=models.UUIDField(primary_key=True,editable=False,default=uuid.uuid4)
    joblogo=models.ImageField(upload_to='images/', default="")
    jobtitle=models.CharField(max_length=50)
    jobcategory=models.CharField(max_length=50)
    companyname=models.CharField(max_length=50)
    location=models.CharField(max_length=50)
    jobtype=models.CharField(max_length=20,choices=job_type,default=None,null=True)
    jobtags=models.CharField(max_length=50)
    salary=models.IntegerField()
    experience=models.CharField(max_length=50)
    responsibilities=models.TextField(blank=True)
    requirements=models.TextField(blank=True)
    benefits=models.TextField( blank=True)
    jobdescription=models.TextField( blank=True)

    def __str__(self):
        return (self.companyname)


class companydetails(models.Model):
   id=models.UUIDField(primary_key=True,editable=False,default=uuid.uuid4)
   logo=models.ImageField(upload_to='companylogos/', default="")
   companyname=models.CharField(max_length=200)
   companysize=models.IntegerField(null=True, blank=True)
   companyaddress=models.CharField(max_length=50)
   companyphone=models.CharField(max_length=50)
   companyemail=models.EmailField(max_length=50)
   companywebsite=models.URLField(max_length=200)
   aboutcompany=models.TextField()
