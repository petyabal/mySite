from django.shortcuts import render, redirect
from .models import Message
from .forms import MessageForm

def main_page(request):
	return render(request, 'mainpage/main_page.html', {})

def your_own_game(request):
	return render(request, 'mainpage/your_own_game.html', {})

def interactive_crossword(request):
	return render(request, 'mainpage/interactive_crossword.html', {})

def phone_payments(request):
	return render(request, 'mainpage/phone_payments.html', {})

def dinnerware_accounting(request):
	return render(request, 'mainpage/dinnerware_accounting.html', {})

def world_war_ii(request):
	return render(request, 'mainpage/world_war_ii.html', {})

def vacation_schedule(request):
	return render(request, 'mainpage/vacation_schedule.html', {})

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
	return render(request, 'mainpage/contacts.html', {'form': form,'messages': message})

def achievements(request):
	return render(request, 'mainpage/achievements.html', {})

def selected_article(request, pk):
	#Вывод конкретной статьи
	article = get_object_or_404(Article, id=pk)
	comment = Comment.objects.filter(comment_article=pk, comment_moderation=True)
	my_comment = None
	if request.user.is_active:
		my_comment = Comment.objects.filter(
			comment_article=pk, 
			comment_moderation=False,
			comment_written_by=request.user)
	if request.method == 'POST':
		form = CommentForm(request.POST)
		if form.is_valid():
			form = form.save(commit=False)
			form.comment_written_by = request.user
			form.comment_article = article
			form.save()
			return redirect(selected_article, pk)
	else:
		form = CommentForm()
	return render(request, 'article/article.html', {'article': article, 'form': form, 
		'comments': comment, 'unmoderated': my_comment,})