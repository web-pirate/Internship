from email.utils import localtime
import uuid
from  django.contrib.auth.models import User
from django.db import models
from pkg_resources import Requirement
job_type={
        ("full-time","full-time"),
        ("part-time","part-time"),
    }
# Create your models here.
class job_profile(models.Model):
    id=models.UUIDField(primary_key=True,editable=False,default=uuid.uuid4)
    jobtitle=models.CharField(max_length=50)
    jobcategory=models.CharField(max_length=50)
    companyname=models.CharField(max_length=50)
    companymail=models.EmailField(max_length=50)
    location=models.CharField(max_length=50)
    jobtype=models.CharField(max_length=20,choices=job_type,default=None,null=True)
    jobtags=models.CharField(max_length=50)
    salary=models.IntegerField()
    experience=models.CharField(max_length=50)
    aboutcompany=models.TextField()
    responsibilities=models.TextField()
    Requirements=models.TextField()
    benefits=models.TextField()
    jobdescription=models.TextField()
