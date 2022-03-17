from operator import mod
from pyexpat import model
from django.db import models

# Create your models here.
class Project(models.Model):
    titel = models.CharField(max_length=200)
    desc = models.TextField()

    create = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.titel