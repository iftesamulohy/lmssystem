from django.contrib import admin
from atexit import register
from lms.models import Classes, Modules, Youtube, Github, Website
# Register your models here.
@admin.register(Youtube)
class YoutubeAdmin(admin.ModelAdmin):
    list_display = ['resourceTitle','resourceDescriptions','rcLinks']

@admin.register(Website)
class YoutubeAdmin(admin.ModelAdmin):
    list_display = ['resourceTitle','resourceDescriptions','rcLinks']

@admin.register(Github)
class YoutubeAdmin(admin.ModelAdmin):
    list_display = ['resourceTitle','resourceDescriptions','rcLinks']

@admin.register(Classes)
class ClassesAdmin(admin.ModelAdmin):
    list_display = ['class_title','classLink']
@admin.register(Modules)
class ClassesAdmin(admin.ModelAdmin):
    list_display = ['nameOfCourse']