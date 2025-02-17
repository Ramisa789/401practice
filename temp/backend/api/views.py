from django.shortcuts import render

#  Create your views here.

# this file handles all the requests and responses 

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Teacher
from .serializers import TeacherSerializer
from django.http import HttpResponse
import requests 

def home_view(request):
    return HttpResponse("Welcome to the teacher management API!")

@api_view(['PUT'])
def update_teacher(request, id):  # id here matches the URL parameter
    try:
        teacher = Teacher.objects.get(id=id)
    except Teacher.DoesNotExist:
        return Response({'message': 'Teacher not found'}, status=404)
    
    serializer = TeacherSerializer(teacher, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)



