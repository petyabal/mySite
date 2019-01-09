from django.urls import path
from . import views

urlpatterns = [
    path('', views.quizzes_list, name='quizzes_list'),
    path('quiz/<pk>/', views.selected_quiz, name='selected_quiz'),
    path('quiz/<pk>/step/<step>/', views.step_of_quiz, name='step_of_quiz'),
    path('quiz/<pk>/step/<step>/log/<log>', views.quiz_log, name='quiz_log'),
    path('quiz/<pk>/result/', views.result, name='result')
]