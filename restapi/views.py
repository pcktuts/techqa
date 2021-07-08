from django.shortcuts import render
from rest_framework import routers, serializers, viewsets
from django.contrib.auth.models import User
from .serializer import UserSerializer, QuestionSerializer, AnswerSerializer

from techqa.models import Question, Answer
# Create your views here.
# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer