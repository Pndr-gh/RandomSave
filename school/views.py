from django.shortcuts import render
from rest_framework.generics import GenericAPIView, ListCreateAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework.mixins import ListModelMixin
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from django.shortcuts import HttpResponse

from .serializers import ClassroomSerializer
from .models import Classroom

class ClassroomAPIViewStaff(ListCreateAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = ClassroomSerializer
    queryset = Classroom.objects.all()

class ClassroomAPIView(ListAPIView):
    serializer_class = ClassroomSerializer
    queryset = Classroom.objects.all()
    
def HelloView(request):
    return HttpResponse ("Hello!")