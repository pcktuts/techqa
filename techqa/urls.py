from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name="home"),
    path('accounts/sign_up/',views.sign_up,name="sign-up"),
    path('<int:question_id>/question', views.show_question, name='show_question'),
    path('add-answer/<int:question_id>', views.add_answer, name='add_answer'),

]