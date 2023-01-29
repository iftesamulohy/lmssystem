from pyexpat import model
from lms.models import Classes, Github, Modules, Website, Youtube
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework_simplejwt.serializers import TokenObtainSerializer
from rest_framework import serializers



class AllUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password']
    def create(self, validated_data):
       user = User.objects.create(
       username = validated_data['username'],
       first_name =validated_data['first_name'],
       last_name =validated_data['last_name'],
       email = validated_data['email'],
       )
       user.set_password(validated_data['password'])
       user.save()
       return user
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
        fields = ('id','class_title','classLink','aboutClass','youtube','website','github')
        depth = 1
    def to_representation(self, instance):
        data = super().to_representation(instance)
        user = self.context['request'].user
        if not user.has_perm('myapp.view_protected_field', instance):
            data.pop('classLink', None)
        return data
class ModulesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Modules
        fields = '__all__'
        depth = 2
    """
    def to_representation(self, instance):
        data = super().to_representation(instance)
        user = self.context['request'].user
        if not user.has_perm('myapp.view_protected_field', instance):
            for i in range(1,len(data.get('classes'))):
                d=data.get('classes')[i]
                d.pop('classLink', None)
                
        return data
        """

class ModulesSerializerw(serializers.ModelSerializer):
    class Meta:
        model = Modules
        fields = '__all__'
        depth = 2
    
    def to_representation(self, instance):
        data = super().to_representation(instance)
        user = self.context['request'].user
        if not user.has_perm('myapp.view_protected_field', instance):
            for i in range(1,len(data.get('classes'))):
                d=data.get('classes')[i]
                d.pop('classLink', None)
                
        return data
        


