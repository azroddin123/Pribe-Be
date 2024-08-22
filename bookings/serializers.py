from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Inquiry


class InquirySerializer(ModelSerializer):
    class Meta :
        model = Inquiry
        fields = "__all__"
        
        