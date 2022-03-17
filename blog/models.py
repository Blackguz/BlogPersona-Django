from turtle import title
from django.db import models

# Create your models here.
class Post(models.Model):
    image = models.ImageField()
    title = models.CharField(max_length= 200)
    descriptcion = models.TextField()
    content = models.TextField()

    create = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    def __str__(self) -> str:
        return self.title