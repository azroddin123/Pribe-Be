from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Inquiry,TestDrive


class InquirySerializer(ModelSerializer):
    class Meta :
        model = Inquiry
        fields = "__all__"

class TestDriveSerializer(ModelSerializer):
    class Meta :
        model = TestDrive
        fields = "__all__"