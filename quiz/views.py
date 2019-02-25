from django.shortcuts import render, get_object_or_404, redirect
# Create your views here.
from .models import Quiz, Step, Question, Answer, ResultsTable
from random import randint
from django.db.models import Q
from django.contrib.auth.decorators import login_required

def quizzes_list(request):
	if request.user.is_active:
		quiz = Quiz.objects.filter(
			Q(quiz_published=True) | Q(quiz_created_by=request.user))
		result = ResultsTable.objects.filter(result_of_user=request.user)
	else:
		quiz = Quiz.objects.filter(quiz_published=True)
		result = None
	return render(request, 'quiz/quizzes_list.html', {'quizzes': quiz, 'results': result})

@login_required
def selected_quiz(request, pk):
	quiz = get_object_or_404(Quiz, quiz_url=pk)
	request.session["questions"] = [] #здесь заводится список для хранения перечня вопросов
	request.session["answers"] = []# список для хранения выбранных вариантов ответов
	result = ResultsTable.objects.filter(result_of_quiz__quiz_url=pk) 
	return render(request, 'quiz/rules.html', {'quiz': quiz, 'results': result})

@login_required
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
		request.session["questions"] += [question.id]
		return render(request, 'quiz/question.html', {'quiz':quiz, 'step': step,# 
			'question': question, 'answers': answer, 'next': next, 'progress': progress, 
			'current': current})#
	else:
		return redirect(result, pk)

@login_required
# запоминание выбранного варианта ответа
def quiz_log(request, pk, step, log):
	request.session["answers"] += [int(log)]
	return redirect(step_of_quiz, pk, step)
#

@login_required
def result(request, pk):
	quiz = get_object_or_404(Quiz, quiz_url=pk)
	questionsLog = request.session["questions"]
	answersLog = request.session["answers"]
	qSet = Question.objects.filter(id__in=questionsLog).order_by('question_of_step__step_number')
	aSet = Answer.objects.filter(answer_to_the_question__in=qSet).order_by(
		'answer_to_the_question__question_of_step__step_number')
	all_steps = qSet.count()
	correct_answers = Answer.objects.filter(id__in=answersLog, 
		answer_status=True).count()
	text = ""
	if correct_answers % 10 == 0 or 5 <= correct_answers % 10 <= 9 or 11 <= correct_answers % 100 <= 14:
		text = str(correct_answers) + ' вопросов'
	elif correct_answers % 10 == 1:
		text = str(correct_answers) + ' вопрос'
	elif 2 <= correct_answers % 10 <= 4:
		text = str(correct_answers) + ' вопроса'
	quiz_result = str(correct_answers / all_steps * 100)
	negative = str(100 - float(quiz_result))
	del request.session["questions"]# удаление списка вопросов
	del request.session["answers"]# удаление списка ответов
	myResult = None
	my_id = None
	if quiz.quiz_published == True:
		myResult = ResultsTable.objects.create(result_of_quiz=quiz, result_of_user=request.user, 
			result_value=float(quiz_result))
		my_id = myResult.id
	all_results = ResultsTable.objects.filter(result_of_quiz=quiz)
	return render(request, 'quiz/result.html', {'quiz':quiz, 'questions': questionsLog, 
		'answers': answersLog, 'questionsSet': qSet, 'answersSet': aSet, 'all_steps': all_steps, 
		'correct_answers': correct_answers, 'quiz_result': quiz_result, 'text': text, 
		'negative': negative, 'my_id': my_id, 'allResults': all_results})
