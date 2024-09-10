from django.contrib import admin
from .models import Inquiry,TestDrive,ContactUs
# Register your models here.
admin.site.register(Inquiry)
admin.site.register(TestDrive)
admin.site.register(ContactUs)