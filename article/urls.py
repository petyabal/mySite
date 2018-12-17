from django.urls import path
from . import views

urlpatterns = [
    path('', views.articles_list, name='articles_list'),
    path('article/<int:pk>', views.selected_article, name='selected_article'),
    path('filter/<int:pk>', views.articles_filter, name='articles_filter'),
]
