import email
from email.headerregistry import Address
from pickle import TRUE
from django.db import models
from psycopg2 import DateFromTicks
from pytz import country_names

# Create your models here.
sex_Choices=(
    ("Male","Male"),
    ("Female","Female"),
    ("Other","Other")
)
class student_details(models.Model):
    username=models.CharField(unique=True,max_length=50)
    profile_image=models.ImageField(upload_to='images', default="")
    name=models.CharField(max_length=50,null=True)
    middlename=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    dob=models.DateTimeField(null=True) 
    sex=models.CharField(max_length=20,choices=sex_Choices,default=None,null=True)
    city=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    country=models.CharField(max_length=50)
    pnumber=models.IntegerField(null=TRUE)
    address=models.TextField(max_length=200)
    email=models.EmailField(max_length=50)
    graduation=models.CharField(max_length=2000)
    college=models.CharField(max_length=200)
    degree=models.CharField(max_length=200)
    additionalinformation=models.TextField(max_length=1000)
    companyname=models.CharField(max_length=50)
    jobposition=models.CharField(max_length=50)
    location=models.CharField(max_length=50)
    DateFrom=models.DateTimeField(null=True)
    DateTo=models.DateTimeField(null=True)
    additionalInformation2=models.TextField(max_length=1000)
    skills=models.CharField(max_length=50)
    skillsproficiency=models.IntegerField(null=True)