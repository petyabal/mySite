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
	request.session["questions"] = [] #здесь заводится список для хранения перечня вопросов
	request.session["answers"] = []# список для хранения выбранных вариантов ответов 
	return render(request, 'quiz/rules.html', {'quiz': quiz})

def step_of_quiz(request, pk, step):
	my_queryset = Question.objects.filter(
		question_of_step__step_of_quiz=pk, question_of_step__step_number=step
		)
	my_step = int(step)#номер текущего шага для progress bar
	if my_queryset:
		step = get_object_or_404(Step, step_of_quiz=pk, step_number=step)
		quiz = Quiz.objects.get(quiz_url=pk)
		question = my_queryset[randint(0, len(my_queryset) - 1)]#выбираем случайный вопрос
		answer = Answer.objects.filter(answer_to_the_question=question)
		next = step.step_number + 1
		all_steps = Step.objects.filter(step_of_quiz=pk).count()#получение числа шагов для progress bar
		progress = str((my_step - 1) / all_steps * 100)#расчет прогресса прохождения
		current = str(1 / all_steps * 100)
		request.session["questions"] += str(question.id)
		log = request.session["answers"]# вывод текущего значения
		return render(request, 'quiz/question.html', {'quiz':quiz, 'step': step,# 
			'question': question, 'answers': answer, 'next': next, 'myLog': log, 
			'progress': progress, 'current': current})#
	else:
		return redirect(result, pk)

# запоминание выбранного варианта ответа
def quiz_log(request, pk, step, log):
	request.session["answers"] += log
	return redirect(step_of_quiz, pk, step)
#

def result(request, pk):
	quiz = get_object_or_404(Quiz, quiz_url=pk)
	questionsLog = request.session["questions"]
	answersLog = request.session["answers"]
	qSet = Question.objects.filter(id__in=questionsLog).order_by('question_of_step__step_number')
	aSet = Answer.objects.filter(answer_to_the_question__in=qSet).order_by(
		'answer_to_the_question__question_of_step__step_number')
	del request.session["questions"]# удаление списка вопросов
	del request.session["answers"]# удаление списка ответов
	return render(request, 'quiz/result.html', {'quiz':quiz, 'questions': questionsLog, 
		'answers': answersLog, 'questionsSet': qSet, 'answersSet': aSet})
