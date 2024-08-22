from django.db import models

# Create your models here.
from portals.models import BaseModel

class Inquiry(BaseModel):
    first_name   = models.CharField(max_length=128,null=True,blank=True)
    last_name    = models.CharField(max_length=128,null=True,blank=True)
    email        = models.CharField(max_length=128,null=True,blank=True)
    phone_no     = models.CharField(max_length=128,null=True,blank=True)
    vehicle_name = models.CharField(max_length=128,null=True,blank=True)
    inquiry_type = models.CharField(max_length=128,null=True,blank=True)
    message      = models.TextField(null=True,blank=True)