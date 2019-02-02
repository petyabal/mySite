from django.shortcuts import render, get_object_or_404, redirect
from .models import Tag, Article, Comment
from .forms import CommentForm
from datetime import datetime, timedelta
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
def articles_list(request):
	#Получение списка статей
	article = Article.objects.all()
	#filter(article_moderation=True)
	tag = Tag.objects.all()
	author = User.objects.all()
	return render(request, "article/articles_list.html", {'articles': article, 
		'tags': tag, 'authors': author})

def selected_article(request, pk):
	#Вывод конкретной статьи
	article = get_object_or_404(Article, id=pk)
	positiveMarks = str(article.article_marked_positive_by.count())
	negativeMarks = str(article.article_marked_negative_by.count())
	comment = Comment.objects.filter(comment_article=pk, comment_moderation=True)
	my_comment = None
	user_choise = 0
	if request.user.is_active:
		my_comment = Comment.objects.filter(
			comment_article=pk, 
			comment_moderation=False,
			comment_written_by=request.user)
		if request.user in article.article_marked_positive_by.all():
			user_choise = 1
		elif request.user in article.article_marked_negative_by.all():
			user_choise = 2
		else: user_choise = 0
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
		'positiveMarks': positiveMarks, 'negativeMarks': negativeMarks, 
		'user_choise': user_choise,	'comments': comment, 'unmoderated': my_comment,})

@login_required
def voting(request, pk, note):
	article = Article.objects.get(id=pk)
	if (note == "+") and (request.user not in article.article_marked_positive_by.all()) and (
	request.user not in article.article_marked_negative_by.all()):
		article_marked_positive_by = article.article_marked_positive_by.add(request.user)
		article.save()
	elif (note == "+") and (request.user in article.article_marked_positive_by.all()) and (
	request.user not in article.article_marked_negative_by.all()):
		article_marked_positive_by = article.article_marked_positive_by.remove(request.user)
		article.save()
	elif (note == "-") and (request.user not in article.article_marked_negative_by.all()) and ( 
	request.user not in article.article_marked_positive_by.all()):
		article_marked_negative_by = article.article_marked_negative_by.add(request.user)
		article.save()
	elif (note == "-") and (request.user in article.article_marked_negative_by.all()) and ( 
	request.user not in article.article_marked_positive_by.all()):
		article_marked_negative_by = article.article_marked_negative_by.remove(request.user)
		article.save()
	else: pass
	return redirect(selected_article, pk)

def articles_date_filter(request, pk):
	#фильтр статей по дате
	article = Article.objects.all()
	tag = Tag.objects.all()
	author = User.objects.all()
	if pk == 'day':
		now = datetime.now() - timedelta(minutes=60*24)
		article = article.filter(article_created__gte=now)
	elif pk == 'week':
		now = datetime.now() - timedelta(minutes=60*24*7)
		article = article.filter(article_created__gte=now)
	elif pk == 'month':
		now = datetime.now() - timedelta(minutes=60*24*30)
		article = article.filter(article_created__gte=now)
	elif pk == 'all':
		#article = article
		return redirect(articles_list)
	return render(request, 'article/articles_list.html', {'articles': article, 'tags': tag, 
		'authors': author})

def articles_tags_filter(request, pk):
	#фильтр статей по тегам
	article = Article.objects.filter(article_tags__tag_title__exact=pk)
	tag = Tag.objects.all()
	author = User.objects.all()
	return render(request, 'article/articles_list.html', {'articles': article, 'tags': tag, 
		'authors': author})

def articles_author_filter(request, pk):
	#фильтр статей по автору
	article = Article.objects.filter(article_written_by__username__exact=pk)
	tag = Tag.objects.all()
	author = User.objects.all()
	return render(request, 'article/articles_list.html', {'articles': article, 'tags': tag, 
		'authors': author})