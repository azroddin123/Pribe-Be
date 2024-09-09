from django.db import models
from accounts.models import User
from portals.models import BaseModel


class Brand(BaseModel):
    name        = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    logo        = models.ImageField(upload_to='brand_logos/', blank=True, null=True)
    def __str__(self):
        return self.name

class Car(BaseModel):
    user                  = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    make                  = models.CharField(max_length=128,null=True,blank=True)
    car_title             = models.CharField(max_length=128,null=True,blank=True)
    car_model             = models.CharField(max_length=128,null=True,blank=True)
    variant               = models.CharField(max_length=128,null=True,blank=True)
    vin                   = models.CharField(max_length=128,null=True,blank=True)
    mileage               = models.DecimalField(max_digits=10, decimal_places=2,null=True,blank=True)
    make_year             = models.PositiveIntegerField(null=True,blank=True)
    
    body_structure_damage = models.CharField(max_length=128,null=True,blank=True)
    flooded_body          = models.CharField(max_length=128,null=True,blank=True)
    rto_location          = models.CharField(max_length=128,null=True,blank=True)
    
    price                 = models.DecimalField(max_digits=10, decimal_places=2,null=True,blank=True)
    ownership             = models.CharField(max_length=128,null=True,blank=True)
    registration_location = models.CharField(max_length=128,null=True,blank=True)
    insurance             = models.CharField(max_length=128,null=True,blank=True)
    insurance_validity    = models.DateField(null=True,blank=True)
    warranty              = models.CharField(max_length=128,blank=True,null=True)
    fuel_type             = models.CharField(max_length=128,null=True,blank=True)
    engine_capacity       = models.CharField(max_length=128,null=True,blank=True)
    transmission          = models.CharField(max_length=128,null=True,blank=True)
    
    condition             = models.TextField(max_length=128,null=True,blank=True)
    key_features          = models.TextField(max_length=128,null=True,blank=True)
    convenience_feature   = models.TextField(max_length=128,null=True,blank=True)
    km_driven             = models.PositiveIntegerField(null=True,blank=True)
    registry_year         = models.PositiveIntegerField(null=True,blank=True)
    registration_number   = models.CharField(max_length=12,null=True,blank=True)

    description           = models.TextField(null=True,blank=True)
    color                 = models.CharField(max_length=30,null=True,blank=True)
    image                 = models.ImageField(upload_to='car_images/',null=True,blank=True)
    status                = models.CharField(max_length=20, choices=[('available', 'Available'), ('sold', 'Sold')],null=True,blank=True)
    location              = models.CharField(max_length=100,null=True,blank=True)
    
    seller_name           = models.CharField(max_length=128,null=True,blank=True)
    contact_no            = models.CharField(max_length=128,null=True,blank=True)
    location              = models.CharField(max_length=128,null=True,blank=True)
    is_approved           = models.BooleanField(default=False)
    
    

class CarImage(BaseModel):
    car               = models.ForeignKey(Car,related_name="car_image",on_delete=models.CASCADE)
    car_image         = models.ImageField(upload_to="car_images")

class Review(BaseModel):
    car         = models.ForeignKey(Car,related_name="reviews",on_delete=models.CASCADE)
    user        = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    name        = models.CharField(max_length=128,null=True,blank=True)
    email       = models.CharField(max_length=128,null=True,blank=True)
    review_text = models.TextField()
    image       = models.ImageField(upload_to="upload_to",null=True,blank=True)
    rating      = models.PositiveIntegerField(default=0)

class Enquiry(BaseModel):
    first_name       = models.CharField(max_length=255,null=True,blank=True)
    last_name        = models.CharField(max_length=255,null=True,blank=True)
    email            = models.CharField(max_length=255,null=True,blank=True)
    vehicle_interest = models.CharField(max_length=255,null=True,blank=True)
    inquiry_type     = models.CharField(max_length=255,null=True,blank=True)
    message          = models.TextField(null=True,blank=True)
    