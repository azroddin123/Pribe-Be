from .models import Car,Brand,CarImage,Review
from rest_framework.serializers import ModelSerializer



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
        
        
        