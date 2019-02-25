from django.contrib import admin
# Register your models here.
from quiz.models import Quiz, Step, Question, Answer, ResultsTable

class QuizAdmin(admin.ModelAdmin):
	list_display = ('quiz_title', 'quiz_url', 'quiz_description', 
		'quiz_created_by', 'quiz_published')
	list_editable = ('quiz_published',)

class StepAdmin(admin.ModelAdmin):
	list_display = ('step_of_quiz',	'step_number')
	list_editable = ('step_number',)

class QuestionAdmin(admin.ModelAdmin):
	list_display = ('question_of_step', 'question_text')

class AnswerAdmin(admin.ModelAdmin):
	list_display = ('answer_to_the_question', 'answer_text', 'answer_status')
	list_editable = ('answer_text', 'answer_status')

class ResultsTableAdmin(admin.ModelAdmin):
	list_display = ('result_of_quiz', 'result_of_user', 'result_datetime', 'result_value')

admin.site.register(Quiz, QuizAdmin)
admin.site.register(Step, StepAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
admin.site.register(ResultsTable, ResultsTableAdmin)