from django.contrib import admin
from comments.models import UserComment , Page

# Register your models here.

admin.site.register((Page , UserComment))

