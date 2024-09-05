from .models import Car,Brand,CarImage,Review,TestDrive,Enquiry
from rest_framework.serializers import ModelSerializer

from rest_framework import serializers

class BrandSerializer(ModelSerializer):
    class Meta :
        model = Brand
        fields = "__all__"

class CarSerializer(ModelSerializer):
    class Meta :
        model  = Car
        fields = "__all__"

class CarImageSerializer(ModelSerializer):
    class Meta :
        model = CarImage
        fields = "__all__"
        

class ReviewSerializer(ModelSerializer):
    class Meta :
        model = Review
        fields ="__all__"
        
class ReviewSerializer1(serializers.ModelSerializer):
    user = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Review
        fields = ['user', 'name', 'email', 'review_text', 'image', 'rating']

    def get_user(self, obj):
        if obj.user:
            return obj.user.username
        return None


class CarSerializer1(ModelSerializer):
    class Meta :
        model = Car
        fields = ["car_title","car_model","price","fuel_type","km_driven","image"]


class CarSerializer1(ModelSerializer):
    class Meta :
        model = Car
        fields = ["car_title","car_model","price","fuel_type","km_driven","image"]    

class CarDetailSerializer(ModelSerializer):
    reviews   = ReviewSerializer1(many=True, read_only=True)
    car_image = CarImageSerializer(many=True,read_only=True)
    user      = serializers.SerializerMethodField(read_only=True)
    car_model = serializers.SerializerMethodField(read_only=True)
    class Meta :
        model = Car 
        fields = ['id','user', 'make', 'car_title', 'car_model', 'variant', 'vin', 'mileage', 'make_year', 'price', 'ownership', 'registration_location', 'insurance', 'insurance_validity', 'fuel_type', 'engine_capacity', 'transmission', 'condition', 'key_features', 'convenience_feature', 'km_driven', 'registry_year', 'registration_number', 'description', 'color', 'image', 'status', 'location', 'seller_name', 'contact_no', 'car_image','reviews']
    
    def get_user(self,obj):
        if obj.user : 
            return obj.user.username 
        return None

    def get_car_model(self,obj):
        if obj.car_model:
            return obj.car_model.name
        return None


class TDSerializer(ModelSerializer):
    class Meta :
        model = TestDrive
        fields ="__all__"
    
class EnquirySerializer(ModelSerializer):
    class Meta :
        model = Enquiry
        fields = "__all__"


