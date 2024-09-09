"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import path,include

from django.http import JsonResponse
def api_status(request):
    """
    View function to return API status message.
    """
    return JsonResponse({'message': 'API Works Here'})
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('accounts/', include('accounts.urls')),
    path("admin/", admin.site.urls),
    path('cars/',include('cars.urls')),
    path('booking/',include('bookings.urls')),
    path('admin-dashboard/',include('PrideAdmin.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL,
#                           document_root=settings.MEDIA_ROOT)
from django.contrib import admin
admin.site.site_header  = 'Pride-Motors'                          
admin.site.index_title  = 'Pride-Motors'                 
admin.site.site_title   = 'Pride-Motors'