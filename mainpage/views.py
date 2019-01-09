from django.shortcuts import render, redirect
from .models import Message, Programm, ProComment
from .forms import MessageForm, ProCommentForm
from django.contrib.auth.models import User

#Главная страница сайта
def main_page(request):
	#is_staff - доступ к административной панели БЕЗ прав изменения сведений в БД
	audience = User.objects.filter(is_superuser=False).count()
	result = []
	if audience % 10 == 0 or 5 <= audience % 10 <= 9 or 11 <= audience % 100 <= 14:
		result = ['На сайте зарегестрировано ', ' пользователей']
	elif audience % 10 == 1:
		result = ['На сайте зарегестрирован ', ' пользователь']
	elif 2 <= audience % 10 <= 4:
		result = ['На сайте зарегестрировано ', ' пользователя']
	return render(request, 'mainpage/main_page.html', {'audience': audience, 'results': result})

def myViewMaker(request, name, html):
    comment = ProComment.objects.filter(comment_frogramm=name, 
    	comment_moderation=True)
    my_comment = None
    if request.user.is_active:
    	my_comment = ProComment.objects.filter(
    		comment_programm=name,
    		comment_moderation=False,
    		comment_written_by=request.user)
    if request.method == 'POST':
    	form = ProCommentForm(request.POST)
    	if form.is_valid():
    		form = form.save(commit=False)
    		form.comment_written_by = Programm.objects.get(programm_title__exact=name)
    		form.save()
    		return redirect(view)
    else:
    	form = ProCommentForm()
    return render(request, html, {'form': form, 'comments': comment, 'unmoderated': my_comment})

#страница "Своей игры" на английском языке на сайте
def your_own_game(request):
	comment = ProComment.objects.filter(comment_programm='your_own_game', 
		comment_moderation=True)
	my_comment = None
	if request.user.is_active:
		my_comment = ProComment.objects.filter(
			comment_programm='your_own_game',
			comment_moderation=False,
			comment_written_by=request.user)
	if request.method == 'POST':
		form = ProCommentForm(request.POST)
		if form.is_valid():
			form = form.save(commit=False)
			form.comment_written_by = request.user
			form.comment_programm = Programm.objects.get(
				programm_title__exact='your_own_game')
			form.save()
			return redirect(your_own_game)
	else:
		form = ProCommentForm()
	return render(request, 'mainpage/your_own_game.html', {'form': form, 
		'comments': comment, 'unmoderated': my_comment})

#страница интерактивного кроссворда на сайте
def interactive_crossword(request):
	comment = ProComment.objects.filter(comment_programm='interactive_crossword', 
		comment_moderation=True)
	my_comment = None
	if request.user.is_active:
		my_comment = ProComment.objects.filter(
			comment_programm='interactive_crossword',
			comment_moderation=False,
			comment_written_by=request.user)
	if request.method == 'POST':
		form = ProCommentForm(request.POST)
		if form.is_valid():
			form = form.save(commit=False)
			form.comment_written_by = request.user
			form.comment_programm = Programm.objects.get(
				programm_title__exact='interactive_crossword')
			form.save()
			return redirect(interactive_crossword)
	else:
		form = ProCommentForm()
	return render(request, 'mainpage/interactive_crossword.html', {'form': form, 
		'comments': comment, 'unmoderated': my_comment})

#страница программы по оплате услуг мобильной связи на сайте
def phone_payments(request):
	comment = ProComment.objects.filter(comment_programm='phone_payments', 
		comment_moderation=True)
	my_comment = None
	if request.user.is_active:
		my_comment = ProComment.objects.filter(
			comment_programm='phone_payments',
			comment_moderation=False,
			comment_written_by=request.user)
	if request.method == 'POST':
		form = ProCommentForm(request.POST)
		if form.is_valid():
			form = form.save(commit=False)
			form.comment_written_by = request.user
			form.comment_programm = Programm.objects.get(
				programm_title__exact='phone_payments')
			form.save()
			return redirect(phone_payments)
	else:
		form = ProCommentForm()
	return render(request, 'mainpage/phone_payments.html', {'form': form, 
		'comments': comment, 'unmoderated': my_comment})

#страница программы учета посуды в ресторане "Спасательный круг" на сайте
def dinnerware_accounting(request):
	comment = ProComment.objects.filter(comment_programm='dinnerware_accounting', 
		comment_moderation=True)
	my_comment = None
	if request.user.is_active:
		my_comment = ProComment.objects.filter(
			comment_programm='dinnerware_accounting',
			comment_moderation=False,
			comment_written_by=request.user)
	if request.method == 'POST':
		form = ProCommentForm(request.POST)
		if form.is_valid():
			form = form.save(commit=False)
			form.comment_written_by = request.user
			form.comment_programm = Programm.objects.get(
				programm_title__exact='dinnerware_accounting')
			form.save()
			return redirect(dinnerware_accounting)
	else:
		form = ProCommentForm()
	return render(request, 'mainpage/dinnerware_accounting.html', {'form': form, 
		'comments': comment, 'unmoderated': my_comment})

#страница "Своей игры" на тему "История Второй мировой войны" на сайте
def world_war_ii(request):
	comment = ProComment.objects.filter(comment_programm='world_war_ii', 
		comment_moderation=True)
	my_comment = None
	if request.user.is_active:
		my_comment = ProComment.objects.filter(
			comment_programm='world_war_ii',
			comment_moderation=False,
			comment_written_by=request.user)
	if request.method == 'POST':
		form = ProCommentForm(request.POST)
		if form.is_valid():
			form = form.save(commit=False)
			form.comment_written_by = request.user
			form.comment_programm = Programm.objects.get(
				programm_title__exact='world_war_ii')
			form.save()
			return redirect(world_war_ii)
	else:
		form = ProCommentForm()
	return render(request, 'mainpage/world_war_ii.html', {'form': form, 
		'comments': comment, 'unmoderated': my_comment})

#страница программы для формирования и ведения графика отпусков в Колэнерго
def vacation_schedule(request):
	comment = ProComment.objects.filter(comment_programm='vacation_schedule', 
		comment_moderation=True)
	my_comment = None
	if request.user.is_active:
		my_comment = ProComment.objects.filter(
			comment_programm='vacation_schedule',
			comment_moderation=False,
			comment_written_by=request.user)
	if request.method == 'POST':
		form = ProCommentForm(request.POST)
		if form.is_valid():
			form = form.save(commit=False)
			form.comment_written_by = request.user
			form.comment_programm = Programm.objects.get(
				programm_title__exact='vacation_schedule')
			form.save()
			return redirect(vacation_schedule)
	else:
		form = ProCommentForm()
	return render(request, 'mainpage/vacation_schedule.html', {'form': form, 
		'comments': comment, 'unmoderated': my_comment})

#страница с контактными данными и формой обратной связи
def contacts(request):
	message = None
	if request.user.is_active:
		message = Message.objects.filter(message_written_by=request.user)
	if request.method == 'POST':
		form = MessageForm(request.POST)
		if form.is_valid():
			form = form.save(commit=False)
			form.message_written_by = request.user
			form.save()
			return redirect(contacts)
	else:
		form = MessageForm()
	return render(request, 'mainpage/contacts.html', {'form': form, 
		'messages': message})

#страница с указанием достижений
def achievements(request):
	return render(request, 'mainpage/achievements.html', {})
