from django.shortcuts import render

# Create your views here.
from cars.models import *
from cars.serializers import * 

# accounts 
from accounts.models import * 
from accounts.serializers import * 
# booking 
from bookings.models import * 
from bookings.serializers import * 

from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from portals.GM2 import GenericMethodsMixin


class UserAPI(GenericMethodsMixin,APIView):
    model            = User
    serializer_class = UserSerializer2
    lookup_field     = "id"

class CarAPI(GenericMethodsMixin,APIView):
    model            = Car
    serializer_class = CarSerializer
    lookup_field     = "id"

class BrandAPI(GenericMethodsMixin,APIView):
    model            = Brand
    serializer_class = BrandSerializer
    lookup_field     = "id"

class TestDriveAPI(GenericMethodsMixin,APIView):
    model            = TestDrive
    serializer_class = TestDriveSerializer
    lookup_field     =  "id"


class EnquiryAPI(GenericMethodsMixin,APIView):
    model            = Enquiry
    serializer_class = EnquirySerializer
    lookup_field     = "id"

class CarImagesAPI(GenericMethodsMixin,APIView):
    model            = CarImage
    serializer_class = CarImageSerializer
    lookup_field     = "id"
    
class ReviewsAPI(GenericMethodsMixin,APIView):
    model = Review
    serializer_class = ReviewSerializer
    lookup_field = "id"

class CarDetailsAPI(GenericMethodsMixin,APIView):
    model = Car
    serializer_class = CarDetailSerializer
    lookup_field = "id"


