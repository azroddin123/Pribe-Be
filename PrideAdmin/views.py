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
from portals.services import paginate_data


class UserAPI(GenericMethodsMixin,APIView):
    model            = User
    serializer_class = UserSerializer2
    lookup_field     = "id"

class CarAPI(GenericMethodsMixin,APIView):
    model            = Car
    serializer_class = CarSerializer
    lookup_field     = "id"
    
    def get(self,request,pk=None,*args,**kwargs):
        try : 
           if pk in ["0", None]:
               data = Car.objects.filter(is_approved=True).order_by('created_on')
               response = paginate_data(Car, CarDetailSerializer, request,data)
               return Response(response,status=status.HTTP_200_OK)
           else : 
               data = Car.objects.get(id=pk)
               serializer = CarDetailSerializer(data)
               return Response({"error" : False,"data" : serializer.data},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error" : True , "message" : str(e) , "status_code" : 400},status=status.HTTP_400_BAD_REQUEST,)

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


class AdminBlogAPI(GenericMethodsMixin,APIView):
    model = Blog
    serializer_class = BlogSerializer
    lookup_field = "id"