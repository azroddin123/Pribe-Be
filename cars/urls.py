from django.urls import path
from .views import * 


urlpatterns = [

path('car-detail',CarAPI.as_view()),
path('car-detail/<str:pk>',CarAPI.as_view()),

path('brand',BrandAPI.as_view()),
path('brand/<str:pk>',BrandAPI.as_view()),

path('car-images',CarImagesAPI.as_view()),
path('car-images/<str:pk>',CarImagesAPI.as_view()),

path('review',ReviewsAPI.as_view()),
path('review/<str:pk>',ReviewsAPI.as_view()),

path('car-detail1',CarDetailsAPI.as_view()),
path('car-detail1/<str:pk>',CarDetailsAPI.as_view()),

path('enquiry',EnquiryAPI.as_view()),
path('enquiry/<str:pk>',EnquiryAPI.as_view()),

path('selling-request',SellingCarAPI.as_view()),
path('selling-request/<str:pk>',SellingCarAPI.as_view())

]