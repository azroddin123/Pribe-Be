from django.shortcuts import render

from portals.GM2 import GenericMethodsMixin

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import Car,Brand,CarImage,Review,Enquiry
from .serializers import (CarSerializer,BrandSerializer,CarImageSerializer,ReviewSerializer,CarDetailSerializer,EnquirySerializer,CarSerializer1,CarSerializer2)
from django.db import transaction
from portals.services import paginate_data,paginate_model_data

class BrandAPI(GenericMethodsMixin,APIView):
    model = Brand
    serializer_class = BrandSerializer
    lookup_field = "id"
    
class CarAPI(GenericMethodsMixin,APIView):
    model  =  Car 
    serializer_class = CarSerializer
    lookup_field  = "id"
    
    def get(self,request,pk=None,*args,**kwargs):
        try : 
           if pk in ["0", None]:
               data = Car.objects.all()
               response = paginate_data(Car, CarDetailSerializer, request,data)
               return Response(response,status=status.HTTP_200_OK)
           else : 
               data = Car.objects.get(id=pk)
               serializer = CarDetailSerializer(data)
               return Response({"error" : False,"data" : serializer.data},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error" : True , "message" : str(e) , "status_code" : 400},status=status.HTTP_400_BAD_REQUEST,)
    
        

    def post(self,request,*args,**kwargs):
        with transaction.atomic():
            try : 
                print(request.data,"--------------------")
                uploaded_images = request.FILES.getlist("car_images")
                print(uploaded_images,"----------------------------")
                serializer = CarSerializer(data=request.data)
                if serializer.is_valid():
                    car = serializer.save()
                    if uploaded_images is not None: 
                        print(car.id,"--------------")
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
                print(request.data)
                uploaded_images = request.FILES.getlist("car_images")
                serializer = CarSerializer(obj,data=request.data,partial=True)
                if serializer.is_valid():
                    car = serializer.save()
                    if not uploaded_images:
                        CarImage.objects.filter(car=pk).delete()
                        car_image_list = [CarImage(car_image=item,car=car) for item in uploaded_images]
                        CarImage.objects.bulk_create(car_image_list)
                    return Response({"error" : False, "data" : serializer.data},status=status.HTTP_202_ACCEPTED)
                return Response({"error" : True , "errors" : serializer.errors},status=status.HTTP_400_BAD_REQUEST)
            except Exception as e :
                return Response({"error" : True , "message" : str(e)},status=status.HTTP_400_BAD_REQUEST)


class AddCarAPI(GenericMethodsMixin,APIView):
    model = Car
    serializer_class = CarSerializer1
    lookup_field = "id"
    
    def post(self,request,*args,**kwargs):
        with transaction.atomic():
            try : 
                uploaded_images = request.FILES.getlist("car_images")
                print("uploaded_images",uploaded_images)
                serializer = CarSerializer2(data=request.data)
                if serializer.is_valid():
                    car = serializer.save()
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

class ReviewsAPI(GenericMethodsMixin,APIView):
    model = Review
    serializer_class = ReviewSerializer
    lookup_field = "id"

class CarDetailsAPI(GenericMethodsMixin,APIView):
    model = Car
    serializer_class = CarDetailSerializer
    lookup_field = "id"

class EnquiryAPI(GenericMethodsMixin,APIView):
    model = Enquiry
    serializer_class = EnquirySerializer
    lookup_field = "id"
    