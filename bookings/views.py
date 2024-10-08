from django.shortcuts import render

# Create your views here.

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from portals.GM2 import GenericMethodsMixin
from rest_framework import status
from .models import Inquiry,TestDrive,ContactUs
from .serializers import InquirySerializer,TestDriveSerializer,ContactUsSerializer


class InquiryAPI(GenericMethodsMixin,APIView):
    model = Inquiry
    serializer_class = InquirySerializer
    lookup_field = "id"
    
class TestDriveAPI(GenericMethodsMixin,APIView):
    model = TestDrive
    serializer_class = TestDriveSerializer
    lookup_field = "id"
    
class ContactAPI(GenericMethodsMixin,APIView):
    model = ContactUs
    serializer_class = ContactUsSerializer
    lookup_field = "id"