from functools import partial
from django.shortcuts import render
from lms.models import Modules, Youtube,Classes
from django.contrib.auth.models import User
#from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import AllUserSerializer, ClassesSerializer, ModulesSerializer, ModulesSerializerw, YoutubeSerializer,UserSerializer
from lms import serializers
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import viewsets
# Create custom function.
from rest_framework import permissions
from rest_framework.authtoken.models import Token
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken

class HasPermissionToViewProtectedField(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.has_perm('myapp.view_protected_field', obj)



# Create your views here.
class RegisterUser(APIView):
    def post(self,requests):
        serializer = UserSerializer(data = requests.data)
        if not serializer.is_valid():
            print(serializer.errors)
            return Response({
            'status':403,
            "errors": serializer.errors,
            "message": "User data not valid"
            
            })
        serializer.save()
        user = User.objects.get(username= serializer.data['username'])
        refresh = RefreshToken.for_user(user)
        return Response({
            'status':200,
            "payload": serializer.data,
            'refresh': str(refresh),
            'access': str(refresh),
            "message": "You logged in successfully"
            
            })
from rest_framework_simplejwt.tokens import AccessToken
class ModulesApi(viewsets.ModelViewSet):
    queryset = Modules.objects.all()
    def get_serializer_class(self):
        try:
            token = self.request.headers.get('Authorization').split()[1]
        except:
            token = None
        if token:
            return ModulesSerializer
        else:
                return ModulesSerializerw
class Userme(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = AllUserSerializer
    def get_queryset(self):
        token = self.request.headers.get('Authorization').split()[1]
        payload = AccessToken(token).payload
        user_id = payload.get('user_id')
        return User.objects.filter(id=user_id)









