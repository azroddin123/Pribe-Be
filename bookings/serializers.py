from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Inquiry,TestDrive,ContactUs


class InquirySerializer(ModelSerializer):
    class Meta :
        model = Inquiry
        fields = "__all__"

class TestDriveSerializer(ModelSerializer):
    class Meta :
        model = TestDrive
        fields = "__all__"
        
class ContactUsSerializer(ModelSerializer):
    class Meta :
        model = ContactUs
        fields  = "__all__"