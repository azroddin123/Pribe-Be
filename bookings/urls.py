from django.urls import path
from .views import InquiryAPI


urlpatterns = [
    
    path('inquiry',InquiryAPI.as_view()),
    path('inquiry/<str:pk>',InquiryAPI.as_view())
    
    
]