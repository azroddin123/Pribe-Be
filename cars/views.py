from django.shortcuts import render

from portals.GM2 import GenericMethodsMixin
from django.db.models import Q
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import Car,Brand,CarImage,Review,Enquiry,Blog
from .serializers import (CarSerializer,BrandSerializer,CarImageSerializer,ReviewSerializer,CarDetailSerializer,EnquirySerializer,CarSerializer1,CarSerializer2,BlogSerializer)
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
               data = Car.objects.filter(is_approved=True).order_by('created_on')
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
                    if uploaded_images: 
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
                    if uploaded_images:
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

class SellingCarAPI(GenericMethodsMixin,APIView):
    model  =  Car 
    serializer_class = CarSerializer
    lookup_field  = "id"
    
    def get(self,request,pk=None,*args,**kwargs):
        try : 
           if pk in ["0", None]:
               data = Car.objects.filter(is_approved=False)
               response = paginate_data(Car, CarDetailSerializer, request,data)
               return Response(response,status=status.HTTP_200_OK)
           else : 
               data = Car.objects.get(id=pk)
               serializer = CarDetailSerializer(data)
               return Response({"error" : False,"data" : serializer.data},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error" : True , "message" : str(e) , "status_code" : 400},status=status.HTTP_400_BAD_REQUEST,)
    
class EnquiryAPI(GenericMethodsMixin,APIView):
    model = Enquiry
    serializer_class = EnquirySerializer
    lookup_field = "id"

class BlogAPI(GenericMethodsMixin,APIView):
    model = Blog
    serializer_class = BlogSerializer
    lookup_field = "id"
    
    def get(self,request,pk=None,*args,**kwargs):
        try : 
           if pk in ["0", None]:
               data = Blog.objects.filter(is_published=True).order_by('created_on')
               response = paginate_data(Blog, BlogSerializer, request,data)
               return Response(response,status=status.HTTP_200_OK)
           else : 
               data = Blog.objects.get(id=pk)
               serializer = BlogSerializer(data)
               return Response({"error" : False,"data" : serializer.data},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error" : True , "message" : str(e) , "status_code" : 400},status=status.HTTP_400_BAD_REQUEST,)



class CarFilterAPI(APIView):
    def get(self,request,*args,**kwargs):
        filter_data = request.data.get('filters', {})
        min_price = request.data.get('min_price', None)  # Get minimum price if provided
        max_price = request.data.get('max_price', None)  # Get maximum price if provided
        
        print(filter_data,"====================")
        
        try:
            cars = Car.objects.filter(**filter_data)
            print(len(cars))
            if min_price is not None and max_price is not None:
                cars = cars.filter(price__gte=min_price, price__lte=max_price)
            elif min_price is not None:
                cars = cars.filter(price__gte=min_price)
            elif max_price is not None:
                cars = cars.filter(price__lte=max_price)
                
            response = paginate_data(Car, CarDetailSerializer, request,cars)
            return Response(response,status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error" : True , "message" : str(e) , "status_code" : 400},status=status.HTTP_400_BAD_REQUEST,)




class CarFilterByPriceAndTypeView(APIView):
    def get(self, request, *args, **kwargs):
        try : 
            # Extract query parameters with defaults as None
            min_price = request.query_params.get('min_price')
            max_price = request.query_params.get('max_price')
            car_type = request.query_params.get('car_type')
            query = Q()
            if car_type:
                query &= Q(car_type=car_type)
            try:
                if min_price is not None:
                    query &= Q(price__gte=float(min_price))
                if max_price is not None:
                    query &= Q(price__lte=float(max_price))
            except ValueError:
                return Response({"error": "Invalid price values"}, status=status.HTTP_400_BAD_REQUEST)
            data = Car.objects.filter(query)
            response = paginate_data(Car, CarDetailSerializer, request,data)
            return Response(response,status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error" : True , "message" : str(e) , "status_code" : 400},status=status.HTTP_400_BAD_REQUEST,)

