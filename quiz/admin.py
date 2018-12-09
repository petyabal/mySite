from django.contrib import admin
# Register your models here.
from quiz.models import Quiz, Step, Question, Answer

class StepAdmin(admin.ModelAdmin):
	list_display = ('step_of_quiz',	'step_number')
	list_editable = ('step_number',)

class QuestionAdmin(admin.ModelAdmin):
	list_display = ('question_of_step', 'question_text')

class AnswerAdmin(admin.ModelAdmin):
	list_display = ('answer_to_the_question', 'answer_text', 'answer_status')
	list_editable = ('answer_text', 'answer_status')

admin.site.register(Quiz)
admin.site.register(Step, StepAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)