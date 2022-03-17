from django.contrib import admin

#models
from .models import Project

# Register your models here.
#admin.site.register(Project)

@admin.register(Project)
class PerfilAdmin(admin.ModelAdmin):
    list_display= ('id', 'titel', 'desc', 'create')
    list_editable = ('titel',)
    list_filter = ('create', 'updated',)
    search_fields= ('title', 'desc', )
