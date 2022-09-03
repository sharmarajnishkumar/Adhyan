from django.db import models
import random as r
from AdhyanApp.models import User

pics=['logo1.jpg','logo2.png','logo3.jpg','logo4.png','logo5.png','logo6.png','logo7.png','logo8.png','logo9.png','logo10.png','logo11.png','logo12.png','logo13.png','logo14.png','logo15.png','logo16.png']
logo=r.choice(pics)

# Create your models here.
class Register(models.Model):
    name=models.CharField(max_length=20)
    mobile=models.CharField(max_length=13)
    gender=models.CharField(max_length=6)
    email=models.EmailField(unique=True)
    address=models.TextField(max_length=60)
    password=models.CharField(max_length=20)
    pic=models.ImageField(upload_to='Profile Pic',default='logo.png')

    def __str__(self):
        return self.name

class Department(models.Model):
    uid = models.ForeignKey(Register,on_delete=models.CASCADE,null=True)
    name=models.CharField(max_length=30)
    headdepartment=models.CharField(max_length=30)
    email=models.EmailField(unique=True)
    mobile=models.CharField(max_length=13)
    no_of_student=models.IntegerField()
    dep_date=models.DateField(null=True)
    date=models.DateField(auto_now_add=True)
    varify=models.BooleanField(default=False)
    reject=models.BooleanField(default=False)
    approve_by = models.CharField(max_length=100,null=True,blank=True)
    
    def __str__(self):
        return self.name

class All_Course(models.Model):
    uid = models.ForeignKey(Register,on_delete=models.CASCADE)
    coname=models.CharField(max_length=50)
    coduration=models.CharField(max_length=30)
    coprice=models.IntegerField()
    codepartment=models.ForeignKey(Department,on_delete=models.CASCADE)
    codiscription=models.TextField(max_length=1000)
    coyear=models.IntegerField()
    copic=models.ImageField(upload_to='course pic',default='python.png')
    covarify=models.BooleanField(default=False)
    coreject=models.BooleanField(default=False)
    approve_by = models.CharField(max_length=100,null=True,blank=True)
    views = models.ManyToManyField(User,related_name='views', blank=True)
    
    def __str__(self):
        return self.coname

class Add_Index(models.Model):
    uid = models.ForeignKey(Register,on_delete=models.CASCADE)
    course = models.ForeignKey(All_Course,on_delete=models.CASCADE)
    topic=models.CharField(max_length=50,)
    material=models.FileField(upload_to="index pdf")
    
    def __str__(self):
        return self.topic
    
class Booking(models.Model):
    student=models.ForeignKey(User,on_delete=models.CASCADE)
    course=models.ForeignKey(All_Course,on_delete=models.CASCADE)
    book_time = models.DateTimeField(auto_now_add=True)
    pay_type = models.CharField(max_length=50,default='online')
    pay_verify = models.BooleanField(default=False)
    pay_id = models.CharField(max_length=30)

    def __str__(self):
        return self.course.coname 
    

class Cart(models.Model):
    student=models.ForeignKey(User,on_delete=models.CASCADE)
    cart=models.ManyToManyField(All_Course,related_name='Cart')
    
    def __str__(self):
        return self.student.name 
    
class Review(models.Model):
    course=models.ForeignKey(All_Course,on_delete=models.CASCADE)
    student = models.ForeignKey(User,on_delete=models.CASCADE)
    msg = models.CharField(max_length=500)
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.msg
    