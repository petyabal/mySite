from django.shortcuts import render, get_object_or_404, redirect
# Create your views here.
from .models import Quiz, Step, Question, Answer
from random import randint
from django.db.models import Q

def quizzes_list(request):
	quiz = Quiz.objects.filter(
		Q(quiz_published=True) | Q(quiz_created_by=request.user))
	return render(request, 'quiz/quizzes_list.html', {'quizzes': quiz})

def selected_quiz(request, pk):
	quiz = get_object_or_404(Quiz, quiz_url=pk)
	request.session["answers"] = 5# здесь устанавливаю первоначальное значение
	return render(request, 'quiz/rules.html', {'quiz': quiz})

def step_of_quiz(request, pk, step):
	my_queryset = Question.objects.filter(
		question_of_step__step_of_quiz=pk, question_of_step__step_number=step
		)
	if my_queryset:
		step = get_object_or_404(Step, step_of_quiz=pk, step_number=step)
		quiz = Quiz.objects.get(quiz_url=pk)
		question = my_queryset[randint(0, len(my_queryset) - 1)]#выбираем случайный вопрос
		answer = Answer.objects.filter(answer_to_the_question=question)
		next = step.step_number + 1
		mylog = request.session["answers"]# вывод текущего значения
		return render(request, 'quiz/question.html', {'quiz':quiz, 'step': step,# 
			'question': question, 'answers': answer, 'next': next, 'mylog': mylog})#
	else:
		return redirect(result, pk)

# изменение значения в зависимости от ответа
def quiz_log(request, pk, step, log):
	mylog = log
	if mylog == 1:
		request.session["answers"] = 1
	elif mylog  == 2:
		request.session["answers"] = 2
	elif mylog == 3:
		request.session["answers"] = 3
	elif mylog == 4:
		request.session["answers"] = 4
	return redirect(step_of_quiz, pk, step)
#

def result(request, pk):
	quiz = get_object_or_404(Quiz, quiz_url=pk)
	mylog = request.session["answers"]# вывод конечного значения
	del request.session["answers"]# удаление конечного значения
	return render(request, 'quiz/result.html', {'quiz':quiz, 'mylog': mylog})
