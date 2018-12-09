from django.forms import ModelForm
from .models import ProComment, Message

class ProCommentForm(ModelForm): #Форма комментариев для ПП
	class Meta:
		model = ProComment
		fields = ('comment_text',)

class MessageForm(ModelForm): #Форма обратной связи
	class Meta:
		model = Message
		fields = ('message_text',)
		