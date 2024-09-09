from django.urls import path
from .views import InquiryAPI,TestDriveAPI


urlpatterns = [
    
    path('inquiry',InquiryAPI.as_view()),
    path('inquiry/<str:pk>',InquiryAPI.as_view()),
    
    path('test-drive',TestDriveAPI.as_view()),
    path('test-drive/<str:pk>',TestDriveAPI.as_view())
    
    
]