from django.db import models
from django.contrib.auth.models import User

# Create your models here.
options=[["video","video"],["images","images"],["zip","zip"]]
class Category(models.Model):
    name=models.CharField(max_length=100,null=True)
    def __str__(self):
        return self.name
class Work(models.Model):
    catdata=models.ForeignKey(Category,max_length=100,null=True,on_delete=models.CASCADE)
    type=models.CharField(choices=options,null=True,max_length=100)
    title=models.CharField(max_length=100,null=True)
    img1 = models.FileField(null=True)
    img2 = models.FileField(null=True)
    img3 = models.FileField(null=True)
    short_description=models.TextField(null=True)
    long_description=models.TextField(null=True)

    def __str__(self):
        return self.title

class Blog(models.Model):
    title=models.CharField(max_length=100,null=True)
    img=models.FileField(max_length=100,null=True)
    video=models.FileField(null=True,blank=True)
    short_description=models.TextField(null=True)
    long_description=models.TextField(null=True)

    def __str__(self):
        return self.title
class message_detail(models.Model):
    name=models.CharField(max_length=100,null=True)
    email=models.EmailField(null=True)
    contact_no=models.IntegerField(max_length=10,null=True)
    message=models.TextField(null=True)
    def __str__(self):
        return self.name



class Home_page(models.Model):
    img1=models.FileField(null=True)
    img2=models.FileField(null=True)
    img3=models.FileField(null=True)
    video=models.FileField(null=True,blank=True)

