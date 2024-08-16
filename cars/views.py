from django.shortcuts import render

from portals.GM2 import GenericMethodsMixin

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import Car,Brand,CarImage
from .serializers import CarSerializer,BrandSerializer,CarImageSerializer
from django.db import transaction

class BrandAPI(GenericMethodsMixin,APIView):
    model = Brand
    serializer_class = BrandSerializer
    lookup_field = "id"
    
class CarAPI(GenericMethodsMixin,APIView):
    model  =  Car 
    serializer_class = CarSerializer
    lookup_field  = "id"

    def post(self,request,*args,**kwargs):
        with transaction.atomic():
            try : 
                uploaded_images = request.FILES.getlist("car_images")
                serializer = CarSerializer(data=request.data)
                if serializer.is_valid():
                    car = serializer.save()
                    car_image_list = [CarImage(car_image=item,car=car) for item in uploaded_images]
                    CarImage.objects.bulk_create(car_image_list)
                    return Response({"error" : False, "data" : serializer.data},status=status.HTTP_201_CREATED)
                return Response({"error" : True , "errors" : serializer.errors},status=status.HTTP_400_BAD_REQUEST)
            except Exception as e :
                return Response({"error" : True , "message" : str(e)},status=status.HTTP_400_BAD_REQUEST)
    
    def put(self,request,pk = None,*args,**kwargs):
        with transaction.atomic():
            try : 
                obj = Car.objects.get(id=pk)
                serializer = CarSerializer(obj,data=request.data,partial=True)
                if serializer.is_valid():
                    car = serializer.save()
                    uploaded_images = request.FILES.getlist("car_images")
                    if uploaded_images : 
                        CarImage.objects.filter(car=id).delete()
                        car_image_list = [CarImage(car_image=item,car=car) for item in uploaded_images]
                    CarImage.objects.bulk_create(car_image_list)
                    return Response({"error" : False, "data" : serializer.data},status=status.HTTP_201_CREATED)
                return Response({"error" : True , "errors" : serializer.errors},status=status.HTTP_400_BAD_REQUEST)
            except Exception as e :
                return Response({"error" : True , "message" : str(e)},status=status.HTTP_400_BAD_REQUEST)


class CarImagesAPI(GenericMethodsMixin,APIView):
    model = CarImage
    serializer_class = CarImageSerializer
    lookup_field = "id"