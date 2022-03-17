from operator import mod
from pyexpat import model
from tabnanny import verbose
from django.db import models

#ckeditor
from ckeditor.fields import RichTextField

# Create your models here.
class Project(models.Model):
    titel = models.CharField(max_length=200, verbose_name='Titulo')
    desc = RichTextField(verbose_name='Descripción')

    create = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')

    class Meta:
        verbose_name='Perfil'
        verbose_name_plural = 'Perfiles'
        ordering = ['-create']

    def __str__(self) -> str:
        return self.titel