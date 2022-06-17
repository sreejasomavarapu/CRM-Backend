from django.contrib import admin
from django.test import tag
from .models import *
# Register your models here.

admin.site.register(Tag)
admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(Order)