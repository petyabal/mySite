from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
User = get_user_model()


class Category(models.Model): #класс категории статей
	class Meta():
		db_table = 'Category'
		verbose_name = 'Категория'
		verbose_name_plural = '1. Категории'
		ordering = ['category_title']

	category_title = models.CharField('Категория', max_length=50)

	def __str__(self):
		return self.category_title


class Tag(models.Model): #класс тегов статей
	class Meta():
		db_table = 'Tag'
		verbose_name = 'Тег'
		verbose_name_plural = '2. Теги'
		ordering = ['tag_title']

	tag_title = models.CharField('Тег', max_length=50);

	def __str__(self):
		return self.tag_title
				

class Article(models.Model): #класс статьи
	class Meta():
		db_table = 'Article'
		verbose_name = 'Статья'
		verbose_name_plural = '3. Статьи'
		ordering = ['-article_created']

	article_title = models.CharField('Заголовок', max_length=100)
	article_written_by = models.ForeignKey(User, 
		on_delete=models.CASCADE, verbose_name='Автор')
	article_category = models.ForeignKey(Category, 
		on_delete=models.SET_NULL, null=True, verbose_name='Категория')
	article_tags = models.ManyToManyField(Tag, verbose_name='Теги') #~
	article_text = models.TextField('Текст статьи')
	article_submission = models.TextField('Краткое изложение', max_length=350)
	article_description = models.CharField('Описание', max_length=100)
	article_image = models.ImageField('Изображение', upload_to='article', blank=True) #-
	article_created = models.DateTimeField('Дата создания', default=timezone.now) 
	article_updated = models.DateTimeField('Дата изменения', default=timezone.now) #-
	article_moderation = models.BooleanField('Модерация', default=False) #-
	article_keywords = models.CharField('Ключевые слова', max_length=50)
	article_marked_positive_by = models.ManyToManyField(User, 
		related_name='marked_positive_by', verbose_name='Оценили положительно', blank=True)
	article_marked_negative_by = models.ManyToManyField(User,
		related_name='marked_negative_by', verbose_name='Оценили отрицательно', blank=True)	

	def __str__(self):
		return self.article_title


class Comment(models.Model): #класс комментария
	class Meta():
		db_table = 'Comment'
		verbose_name = 'Комментарий'
		verbose_name_plural = '4. Комментарии'
		ordering = ['-comment_created']
		
	comment_written_by = models.ForeignKey(User, 
		on_delete=models.CASCADE, verbose_name='Автор')
	comment_article = models.ForeignKey(Article, 
		on_delete=models.CASCADE, verbose_name='Статья')
	comment_text = models.TextField('Текст комментария')
	comment_created = models.DateTimeField('Добавлен', auto_now_add=True)
	comment_moderation = models.BooleanField('Модерация', default=False)

	def __str__(self):
		return '{}'.format(self.comment_written_by)


