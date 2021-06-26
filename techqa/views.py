from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

from .models import Question, Answer
# Create your views here.
@login_required
def index(request):
    all_questions = Question.objects.all().prefetch_related('question_author').order_by('-id')
    #all_answers = Answer.objects.all().prefetch_related('question_id').order_by('-id') 
    paginator = Paginator(all_questions, 10) 

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {'all_questions_page_obj': page_obj}
    return render(request,'techqa/index.html', context)
def sign_up(request):
    context = {}
    form = UserCreationForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            user = form.save()
            login(request,user)
            return render(request,'techqa/index.html')
    context['form']=form
    return render(request,'registration/sign_up.html',context)
def show_question(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
        answers = Answer.objects.filter(question_id=question_id)
       
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    except Answer.DoesNotExist:
        answers = None
    return render(request,'question/show.html', {'question': question, 'answers': answers})