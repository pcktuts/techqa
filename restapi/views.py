from django.shortcuts import render
from rest_framework import routers, serializers, viewsets
from django.contrib.auth.models import User
from .serializer import UserSerializer
# Create your views here.
# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer