from pyexpat import model
from lms.models import Classes, Github, Modules, Website, Youtube
from rest_framework import serializers

class YoutubeSerializer(serializers.ModelSerializer):
   class Meta:
    model = Youtube
    fields = '__all__'

class GithubSerializer(serializers.ModelSerializer):
   class Meta:
    model = Github
    fields = '__all__'

class WebsiteSerializer(serializers.ModelSerializer):
   class Meta:
    model = Website
    fields = '__all__'
class ClassesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classes
        fields = '__all__'
        depth = 1
class ModulesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Modules
        fields = '__all__'
        depth = 2

