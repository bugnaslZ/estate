from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Agent(models.Model):
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='agents',default='vector.jpg')
    domain = models.CharField(max_length=200)
    twitter = models.CharField(max_length=200)
    instagram = models.CharField(max_length=200)
    facebook = models.CharField(max_length=200)
    linkdin = models.CharField(max_length=200)
    status = models.BooleanField(default=False)
   

class Count(models.Model):
    score = models.IntegerField(default=5)

    def __str__(self) :
        return str(self.score)
    
class Tester(models.Model):
    tester = models.CharField(max_length=220)
    logo = models.ImageField(default='mdma66.png')
    comment = models.TextField()
    star = models.ForeignKey(Count,on_delete=models.DO_NOTHING)
    status = models.BooleanField(default=False)

    def __str__(self) :
        return self.tester
    
    def star_count(self):
        return range(self.star.score)

class Category(models.Model):
    name = models.CharField(max_length=220)

    def __str__(self):
        return self.name




