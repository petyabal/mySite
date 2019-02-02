from django.urls import path
from . import views
from django.contrib.auth.views import (
	PasswordResetView, PasswordResetDoneView, 
	PasswordResetConfirmView, PasswordResetCompleteView
	)

urlpatterns = [
    path('exit/', views.exit_view, name='exit_view'),
	path('login/', views.login_view, name='login_view'),
    path('logout/', views.logout_view, name='logout_view'),
	path('signup/', views.register_view, name='register_view'),
	path('profile/', views.profile_view, name='profile_view'),
	path('profile/password/', views.edit_password, name='edit_password'),
	path('profile/password/reset/', PasswordResetView.as_view(), name='password_reset'),
	path('profile/password/reset/done', PasswordResetDoneView.as_view(), name='password_reset_done'),
	path('profile/password/reset/<uidb64>/<token>', PasswordResetConfirmView.as_view(), 
		name='password_reset_confirm'),
	path('profile/password/reset/complete/', PasswordResetCompleteView.as_view(), name='password_reset_complete')
]
