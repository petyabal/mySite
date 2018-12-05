from django.urls import path
from . import views

urlpatterns = [
    path('exit/', views.exit_view, name='exit_view'),
	path('login/', views.login_view, name='login_view'),
    path('logout/', views.logout_view, name='logout_view'),
	path('signup/', views.register_view, name='register_view'),
	path('profile/', views.profile_view, name='profile_view'),
	path('profile/password/', views.edit_password, name='edit_password')
]
