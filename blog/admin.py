import imp
from re import search
from django.contrib import admin

#Models
from .models import Post

# Register your models here.

#admin.site.register(Post)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display= ('id', 'image', 'title', 'descriptcion', 'create')
    list_display_links = ('id','title',)
    list_filter = ('create', 'updated',)
    search_fields= ('title', 'descriptcion', )


    readonly_fields = ('create', 'updated')