from django.shortcuts import render

# Create your views here.
from cars.models import *
from cars.serializers import * 
from portals.GM2 import GenericMethodsMixin
from accounts.models import * 
from accounts.serializers import * 

from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

class UserAPI(GenericMethodsMixin,APIView):
    model = User
    serializer_class = UserSerializer2
    lookup_field = "id"

class CarAPI(GenericMethodsMixin,APIView):
    model = Car
    serializer_class = CarSerializer
    lookup_field  = "id"

class BrandAPI(GenericMethodsMixin,APIView):
    model = Brand
    serializer_class = BrandSerializer
    lookup_field = "id"

class TestDriveAPI(GenericMethodsMixin,APIView):
    model = TestDrive
    serializer_class = TestDrive
    lookup_field = "id"

class ReviewAPI(GenericMethodsMixin,APIView):
    model = Review
    serializer_class = ReviewSerializer
    lookup_field = "id"

class EnquiryAPI(GenericMethodsMixin,APIView):
    model = Enquiry
    serializer_class = EnquirySerializer
    lookup_field = "id"