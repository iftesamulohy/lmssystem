from functools import partial
from django.shortcuts import render
from lms.models import Modules, Youtube,Classes
#from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ClassesSerializer, ModulesSerializer, YoutubeSerializer
from lms import serializers
from rest_framework.views import APIView
from rest_framework import status
# Create your views here.

# Create your views here.
class ModulesApi(APIView):
    def get(self,request,pk=None,format = None):

        id = pk
        if id is not None:
            modu = Modules.objects.get(id=id)
            serializer = ModulesSerializer(modu)
            return Response(serializer.data)
        modu = Modules.objects.all()
        serializer = ModulesSerializer(modu,many=True)
        return Response({
        'status':True,
        'message': "All Module data fetched",
        'data':serializer.data
        })