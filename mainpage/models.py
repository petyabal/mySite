from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.
class Programm(models.Model): #класс программы
	class Meta():
		db_table = 'Programm'
		verbose_name = 'Программа'
		verbose_name_plural = '1. Программы'

	programm_title = models.CharField('Название программы', max_length=80, primary_key=True)

	programm_marked_positive_by = models.ManyToManyField(User, 
		related_name='programm_marked_positive_by', verbose_name='Оценили положительно', blank=True)
	programm_marked_negative_by = models.ManyToManyField(User,
		related_name='programm_marked_negative_by', verbose_name='Оценили отрицательно', blank=True)

	def __str__(self):
		return self.programm_title
'''
programms_list = [
    'your_own_game', 'interactive_crossword', 'phone_payments', 
    'dinnerware_accounting', 'world_war_ii', 'vacation_schedule'
]
for i in programms_list:
	myProgramm = Programm.objects.filter(programm_title__exact=i)
	if not myProgramm: 
		myProgramm = Programm.objects.create(programm_title=i)'''
#exact-точное совпадение,contains-регистрозависимый поиск,iexact-регистронезависимый поиск


class ProComment(models.Model): #класс комментария
	class Meta():
		db_table = 'ProComment'
		verbose_name = 'Комментарий'
		verbose_name_plural = '2. Комментарии'
		ordering = ['-comment_created']
		
	comment_written_by = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
	comment_programm = models.ForeignKey(Programm, 
		on_delete=models.CASCADE, verbose_name='Программа')
	comment_text = models.TextField('Текст комментария')
	comment_created = models.DateTimeField('Добавлен', auto_now_add=True)
	comment_moderation = models.BooleanField('Модерация', default=False)

	def __str__(self):
		return '{}'.format(self.comment_written_by)


class Message(models.Model):#класс сообщения с формы обратной связи
	class Meta():
		db_table = 'Message'
		verbose_name = 'Сообщение'
		verbose_name_plural = '3. Сообщения'
		ordering = ['-message_sent']

	message_written_by = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
	message_text = models.TextField('Текст сообщения')
	message_sent = models.DateTimeField('Сообщение отправлено', auto_now_add=True)

	def __str__(self):
		return '{}'.format(self.message_written_by)

