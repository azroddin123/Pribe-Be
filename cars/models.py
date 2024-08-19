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
    user                = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    make                = models.CharField(max_length=128)
    car_title           = models.CharField(max_length=128)
    car_model           = models.ForeignKey(Brand, on_delete=models.CASCADE)
    variant             = models.CharField(max_length=128)
    vin                 = models.CharField(max_length=128)
    mileage             = models.DecimalField(max_digits=10, decimal_places=2)
    make_year           = models.PositiveIntegerField()
    
    price               = models.DecimalField(max_digits=10, decimal_places=2)
    ownership           = models.CharField(max_length=128)
    registration_location = models.CharField(max_length=128)
    insurance             = models.CharField(max_length=128)
    insurance_validity    = models.DateField(null=True,blank=True)
    
    fuel_type           = models.CharField(max_length=128)
    engine_capacity     = models.CharField(max_length=128)
    transmission        = models.CharField(max_length=128)
    
    condition           = models.CharField(max_length=128)
    key_features        = models.CharField(max_length=128)
    convenience_feature = models.CharField(max_length=128)
    km_driven           = models.PositiveIntegerField()
    registry_year       = models.PositiveIntegerField()
    registration_number = models.CharField(max_length=12)

    description         = models.TextField()
    color               = models.CharField(max_length=30)
    image               = models.ImageField(upload_to='car_images/')
    status              = models.CharField(max_length=20, choices=[('available', 'Available'), ('sold', 'Sold')])
    location            = models.CharField(max_length=100)
    
    seller_name         = models.CharField(max_length=128)
    contact_no          = models.CharField(max_length=128)
    location            = models.CharField(max_length=128)

class CarImage(BaseModel):
    car = models.ForeignKey(Car,on_delete=models.CASCADE)
    car_image = models.ImageField(upload_to="car_images")

class Review(BaseModel):
    name        = models.CharField(max_length=128,null=True,blank=True)
    email       = models.CharField(max_length=128,null=True,blank=True)
    review_text = models.TextField()
    image       = models.ImageField(upload_to="upload_to",null=True,blank=True)
    rating      = models.PositiveIntegerField(default=0)
    