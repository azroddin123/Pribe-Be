from django.db import models

# Create your models here.
from portals.models import BaseModel
from accounts.models import User
from cars.models import Car

class Inquiry(BaseModel):
    first_name   = models.CharField(max_length=128,null=True,blank=True)
    last_name    = models.CharField(max_length=128,null=True,blank=True)
    email        = models.CharField(max_length=128,null=True,blank=True)
    phone_no     = models.CharField(max_length=128,null=True,blank=True)
    vehicle_name = models.CharField(max_length=128,null=True,blank=True)
    inquiry_type = models.CharField(max_length=128,null=True,blank=True)
    message      = models.TextField(null=True,blank=True)
    is_approved         = models.BooleanField(default=False)
    

class TestDrive(BaseModel):
    user               = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    car                = models.ForeignKey(Car,related_name="test_drive",on_delete=models.CASCADE,null=True,blank=True)
    full_name          = models.CharField(max_length=128,null=True,blank=True)
    email_address      = models.CharField(max_length=128,null=True,blank=True)
    date               = models.DateField(null=True,blank=True)
    time               = models.CharField(max_length=128,null=True,blank=True)
    car_model          = models.CharField(max_length=128,null=True,blank=True)
    preferred_location = models.CharField(max_length=128,null=True,blank=True)
    is_approved        = models.BooleanField(default=False)
    notes              = models.TextField(null=True,blank=True)
    
    