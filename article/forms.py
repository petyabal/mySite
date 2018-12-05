from django.forms import ModelForm
from .models import Comment

class CommentForm(ModelForm): #Форма комментариев
	class Meta:
		model = Comment
		fields = ('comment_text',)
		