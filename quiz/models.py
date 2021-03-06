from django.db import models
# Create your models here.
from django.contrib.auth import get_user_model
User = get_user_model()


class Quiz(models.Model): #класс темы тестирования
	class Meta():
		db_table = 'Quiz'
		verbose_name = 'Онлайн-тестирование'
		verbose_name_plural = '1. Онлайн-тестирования'
		ordering = ['quiz_title']

	quiz_url = models.CharField('Url-адрес(a-z_0-9)', max_length=15, primary_key=True)
	quiz_title = models.CharField('Тема', max_length=50)
	quiz_description = models.CharField('Описание тестирования', max_length=250)
	quiz_created_by = models.ForeignKey(User, on_delete=models.SET_NULL, 
		verbose_name='Добавлено пользователем', null=True)
	quiz_published = models.BooleanField('Тестирование доступно для прохождения', 
		default=False)

	def __str__(self):
		return '{}'.format(self.quiz_url)


#шаг объединяет в себе несколько вопросов, из которых выбирается один 
class Step(models.Model): #класс шага
	class Meta():
		db_table = 'Step'
		verbose_name = 'Шаг'
		verbose_name_plural = '2. Шаги'
		#ordering = ['step_of_quiz__quiz']

	step_of_quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, 
		verbose_name='Тема тестирования (url-адрес)')
	step_number = models.SmallIntegerField('Номер шага')

	def __str__(self):
		return '{}'.format(self.step_number)


class Question(models.Model): #класс вопроса
	class Meta():
		db_table = 'Question'
		verbose_name = 'Вопрос'
		verbose_name_plural = '3. Вопросы'
		#ordering = ['']

	question_of_step = models.ForeignKey(Step, on_delete=models.CASCADE, 
		verbose_name='Шаг')
	question_text = models.CharField('Вопрос', max_length=100)
	question_image = models.ImageField('Изображение', upload_to='quiz', blank=True)
	question_reference = models.TextField('Справка', blank=True)

	def __str__(self):
		return self.question_text


class Answer(models.Model): #класс ответа
	class Meta():
		db_table = 'Answer'
		verbose_name = 'Ответ'
		verbose_name_plural = '4. Ответы'
		#ordering = ['']

	answer_to_the_question = models.ForeignKey(Question, 
		on_delete=models.CASCADE, verbose_name='Вопрос')
	answer_text = models.CharField('Текст ответа', max_length=100)
	answer_image = models.ImageField('Изображение', upload_to='quiz', blank=True)
	answer_status = models.BooleanField('Верный ответ', default=False)

	def __str__(self):
		return self.answer_text


class ResultsTable(models.Model): #класс таблицы результатов
	class Meta():
		db_table = 'ResultsTable'
		verbose_name = 'Таблица результатов'
		verbose_name_plural = 'Таблица результатов'
		ordering = ['-result_value']

	result_of_quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, verbose_name='Тестирование')
	result_of_user = models.ForeignKey(User, on_delete=models.SET_NULL, verbose_name='Участник', null=True)
	result_datetime = models.DateTimeField('Тестирование пройдено', auto_now_add=True)
	result_value = models.FloatField('Результат (%)')

	def __str__(self):
		return str(self.result_of_quiz)
