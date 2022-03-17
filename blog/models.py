from tabnanny import verbose
from turtle import title
from django.db import models

#ckeditor
from ckeditor.fields import RichTextField

# Create your models here.
class Post(models.Model):
    image = models.ImageField(verbose_name='Imagen')
    title = models.CharField(max_length= 200, verbose_name='Titulo')
    descriptcion = models.TextField(verbose_name='Descripción')
    content = RichTextField(verbose_name='Contenido')

    create = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')

    class Meta:
        verbose_name='Publicación'
        verbose_name_plural = 'Publicaciones'
        ordering = ['-create']

    def __str__(self) -> str:
        return self.title