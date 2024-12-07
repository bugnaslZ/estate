from django.db import models
from root.models import Category
# Create your models here.
class Service(models.Model):
    name = models.CharField(max_length=220)
    desc = models.TextField()
    categorys = models.ManyToManyField(Category)

    def __str__(self) :
        return self.name
