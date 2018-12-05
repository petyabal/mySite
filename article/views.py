from django.shortcuts import render, get_object_or_404, redirect
from .models import Article, Comment
from .forms import CommentForm
from datetime import datetime, timedelta

# Create your views here.
def articles_list(request):
	#Получение списка статей
	article = Article.objects.all()
	#filter(article_moderation=True)
	return render(request, "article/articles_list.html", {"articles": article})

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

def articles_filter(request, pk):
	#фильтр статей по дате
	article = Article.objects.all()
	if pk == 1:
		now = datetime.now() - timedelta(minutes=60*24)
		article = article.filter(article_created__gte=now)
	elif pk == 2:
		now = datetime.now() - timedelta(minutes=60*24*7)
		article = article.filter(article_created__gte=now)
	elif pk == 3:
		now = datetime.now() - timedelta(minutes=60*24*30)
		article = article.filter(article_created__gte=now)
	elif pk == 4:
		article = article
	return render(request, 'article/articles_list.html', {'articles': article})