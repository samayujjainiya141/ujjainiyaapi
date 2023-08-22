from django.db import models 
# Create your models here. 
class Student(models.Model): 
    sname=models.CharField(max_length=20) 
    branch=models.CharField(max_length=20) 
    email=models.EmailField(max_length=20) 
    def __str__(self): 
        return self.sname