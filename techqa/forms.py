from django import forms
from .models import Answer
class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['answer', 'question_id', 'answer_author']