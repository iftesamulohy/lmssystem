from django.db import models

# Create your models here.

class Youtube(models.Model):
    resourceTitle = models.CharField(max_length = 100)
    resourceDescriptions = models.TextField()
    rcLinks=models.URLField(max_length=200)

class Website(models.Model):
    resourceTitle = models.CharField(max_length = 100)
    resourceDescriptions = models.TextField()
    rcLinks=models.URLField(max_length=200)


class Github(models.Model):
    resourceTitle = models.CharField(max_length = 100)
    resourceDescriptions = models.TextField()
    rcLinks=models.URLField(max_length=200)

class Classes(models.Model):
    class_title = models.CharField(max_length = 100)
    classLink = models.URLField(max_length=200)
    aboutClass=models.TextField()
    youtube= models.ManyToManyField(Youtube)
    website= models.ManyToManyField(Website)
    github = models.ManyToManyField(Github)
class Modules(models.Model):
    nameOfCourse = models.CharField(max_length = 100)
    uploadTime = models.DateTimeField()
    descriptions=models.TextField()
    classes = models.ManyToManyField(Classes)