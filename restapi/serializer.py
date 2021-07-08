from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from techqa.models import Question, Answer

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff', 'password']
    
    def create(self, validated_data):
        user = super(UserSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

class AnswerSerializer(serializers.HyperlinkedModelSerializer):
    question = serializers.CharField(source='question_id.title')
    class Meta:
        model = Answer
        fields = ['question', 'answer', 'answer_author']


class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    answers = serializers.SerializerMethodField()
    question_author = serializers.CharField(source='question_author.username')
    class Meta:
        model = Question
        fields = ['title', 'content', 'question_author', 'created_at', 'answers']
    def get_answers(self, obj):
        try:
            answers = Answer.objects.filter(question_id=obj.pk)
            answers = [
                        {"answer": u.answer, 
                        "is_accepted_answer": u.is_accepted_answer, 
                        "answer_author": u.answer_author.username,
                        "created_at": u.created_at
                        } 
                        for u in answers
                    ]
       
        except Answer.DoesNotExist:
            answers = None
      
        return list(answers)

