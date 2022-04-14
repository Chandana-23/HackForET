from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField( max_length=250)
    email = models.EmailField(max_length=254)
    pwd = models.CharField(max_length=50)
    branch = models.CharField(max_length=50)
    contact = models.CharField(max_length=50)
    role = models.CharField(max_length=50,default='student')
    auth = models.BooleanField(default=False)

class Teacher(models.Model):
    name = models.CharField( max_length=250)
    email = models.EmailField(max_length=254)
    pwd = models.CharField(max_length=50)
    branch = models.CharField(max_length=50)
    contact = models.CharField(max_length=50)
    role = models.CharField(max_length=50,default='teacher')
    auth = models.BooleanField(default=False)
class Blog(models.Model):
    email = models.EmailField(max_length=254)
    role = models.CharField(max_length=50)
    content = models.TextField()
    img = models.ImageField(upload_to='media/')
