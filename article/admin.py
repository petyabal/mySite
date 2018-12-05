from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from article.models import Category, Article, Comment, Tag
from mainpage.models import Programm, ProComment, Message


# Register your models here.
class ArticleAdminEditor(SummernoteModelAdmin, admin.ModelAdmin):
	summer_note_fields = ('article_text', 'article_submission')
	list_display = ('article_title', 'article_written_by', 'article_created')
	list_editable = ('article_written_by',)
	list_filter = ('article_written_by', 'article_created')
	search_fields = ('article_title', 'article_written_by__username')
	exclude = ['article_reputation'] 
	#вместо fields = ['article_title', 'article_text', 'article_date']

class CommentAdmin(admin.ModelAdmin):
	list_display = ('comment_written_by', 'comment_article', 'comment_text', 'comment_created', 'comment_moderation')


admin.site.register(Article, ArticleAdminEditor)
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Comment, CommentAdmin)

admin.site.register(Programm)
admin.site.register(ProComment)
admin.site.register(Message)
