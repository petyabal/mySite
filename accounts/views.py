from django.shortcuts import render, redirect
# Create your views here.
from django.contrib.auth import (authenticate, get_user_model, 
	login, logout, update_session_auth_hash)
from .forms import (UserLoginForm, UserRegisterForm, 
	EditProfileForm)
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import (UserChangeForm, 
	PasswordChangeForm)


def login_view(request):
	next = request.GET.get('next')
	form = UserLoginForm(request.POST or None)
	if form.is_valid():
		username = form.cleaned_data.get('username')
		password = form.cleaned_data.get('password')
		user = authenticate(username=username, password=password)
		login(request, user)
		if next:
			return redirect(next)
		return redirect('/')
	return render(request, 'login.html', {'form': form,})

def register_view(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')
	else:
		form = UserRegisterForm()
	return render(request, 'signup.html', {'form': form})

def logout_view(request):
	logout(request)
	return redirect('/')

@login_required
def exit_view(request):
	return render(request, 'exit.html', {})

@login_required
def profile_view(request):
	if request.method == 'POST':
		form = EditProfileForm(request.POST, instance=request.user)
		if form.is_valid():
			form.save()
			return redirect('profile_view')
	else:
		form = EditProfileForm(instance=request.user)
		return render(request, 'profile.html', {'form': form})

def edit_password(request):
	if request.method == 'POST':
		form = PasswordChangeForm(data=request.POST, user=request.user)
		if form.is_valid():
			form.save()
			update_session_auth_hash(request, form.user)
			return redirect('profile_view')
		else:
			return redirect('edit_password')
	else:
		form = PasswordChangeForm(user=request.user)
		return render(request, 'profile.html', {'form': form})