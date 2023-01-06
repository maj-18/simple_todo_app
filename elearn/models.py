from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserType(models.Model):
    owner=models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    user_type=models.CharField(max_length=20,default='admin')

class Courses(models.Model):
    course_name=models.CharField(max_length=50)
    course_price=models.IntegerField()

class Exam(models.Model):
    exam_name=models.CharField(max_length=101)
    course=models.ForeignKey(Courses,on_delete=models.CASCADE,default='python')
    exam_time=models.DateTimeField(null=True,blank=True)

class Marks(models.Model):
    owner=models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    exam=models.ForeignKey(Exam,on_delete=models.CASCADE,default=1)
    course=models.ForeignKey(Courses,on_delete=models.CASCADE,default=1)
    mark=models.IntegerField()
    maxmarks=models.IntegerField()

class Materials(models.Model):
    course=models.ForeignKey(Courses,on_delete=models.CASCADE,default='python')
    material=models.FileField(upload_to='media/')

class Teachprofile(models.Model):
    owner=models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    name=models.CharField(max_length=51)
    dob=models.DateField()
    address=models.TextField()
    place=models.CharField(max_length=51)
    city=models.CharField(max_length=51)
    state=models.CharField(max_length=51)
    course=models.ForeignKey(Courses,on_delete=models.CASCADE,default=1)

class Stuprofile(models.Model):
    owner=models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    name=models.CharField(max_length=51)
    dOB=models.DateField()
    address=models.TextField()
    place=models.CharField(max_length=51)
    city=models.CharField(max_length=51)
    state=models.CharField(max_length=51)

class Mycourses(models.Model):
    course=models.ForeignKey(Courses,on_delete=models.CASCADE,default=1)
    owner=models.ForeignKey(User,on_delete=models.CASCADE,default=1)