from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.Department)

@admin.register(models.Register)
class UserAdmin(admin.ModelAdmin):
    list_display = ['name','email','mobile','gender']

@admin.register(models.All_Course)
class UserAdmin(admin.ModelAdmin):
    list_display = ['coname','coduration','coprice','codepartment','codiscription','coyear']

@admin.register(models.Add_Index)
class UserAdmin(admin.ModelAdmin):
    list_display = ['topic','material']
    
@admin.register(models.Booking)
class UserAdmin(admin.ModelAdmin):
    list_display = ['book_time','pay_type','pay_verify','pay_id']

@admin.register(models.Cart)
class UserAdmin(admin.ModelAdmin):
    list_display = ['student']
    
@admin.register(models.Review)
class UserAdmin(admin.ModelAdmin):
     list_display = ['student','course','date','msg']