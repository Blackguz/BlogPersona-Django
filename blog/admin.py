import imp
from django.contrib import admin

#Models
from .models import Post

# Register your models here.

admin.site.register(Post)