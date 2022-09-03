from django.contrib import admin

# Register your models here.
from .models import *

@admin.register(Enquiry)
class UserAdmin(admin.ModelAdmin):
    list_display = ['name','mobile','email','city','des']

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['name','mobile','email','address']
    
