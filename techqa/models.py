from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Question(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    question_author = models.ForeignKey(User, on_delete=models.CASCADE)   
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Answer(models.Model):
    question_id =models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.TextField()
    is_accepted_answer =models.BooleanField(default=False)
    answer_author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)