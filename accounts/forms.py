from django import forms
from django.contrib.auth import authenticate, get_user_model

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class UserLoginForm(forms.Form):
					
	username = forms.CharField(label='Логин')
	password = forms.CharField(widget=forms.PasswordInput, label='Пароль')

	def clean(self, *args, **kwargs):
		username = self.cleaned_data.get('username')
		password = self.cleaned_data.get('password')
		if username and password:
			user = authenticate(username=username, password=password)
			if not user:
				raise forms.ValidationError('Неправильный логин и/или пароль! / ' +
					'The username and/or password you specified are not correct!')		
			if not user.is_active:
				raise forms.ValidationError('Ваша учетная запись заблокирована! / ' + 
					'The login and the password is valid, but the account has been disabled!')
		return super(UserLoginForm, self).clean(*args, **kwargs)

class UserRegisterForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'first_name', 'last_name', 'email', 
			'password1', 'password2']

	username = forms.CharField(label='Логин*')
	first_name = forms.CharField(label='Имя', required=False)
	last_name = forms.CharField(label='Фамилия', required=False)
	email = forms.EmailField(label='Адрес эл. почты',required=False)
	password1 = forms.CharField(widget=forms.PasswordInput, label='Пароль*')
	password2 = forms.CharField(widget=forms.PasswordInput, label='Пароль (повторно)*')

	def save(self, commit=True):
		user = super(UserRegisterForm, self).save(commit=False)
		user.first_name = self.cleaned_data.get('first_name')
		user.last_name = self.cleaned_data.get('last_name')
		email = self.cleaned_data.get('email')
		if commit:
			user.save()
		return user

class EditProfileForm(UserChangeForm):
	class Meta:
		model = User
		fields = ('email', 'first_name', 'last_name', 'password')
		exclude = ()

	email = forms.EmailField(label='Адрес эл. почты', required=False)
	first_name = forms.CharField(label='Имя', required=False)
	last_name = forms.CharField(label='Фамилия', required=False)
	password = forms.CharField(label='Пароль (зашифрован, для изменения нажмите кнопку внизу)')