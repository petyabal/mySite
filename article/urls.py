from django.urls import path
from . import views

urlpatterns = [
    path('', views.articles_list, name='articles_list'),
    path('article/<int:pk>', views.selected_article, name='selected_article'),
    path('date_filter/<pk>', views.articles_date_filter, name='articles_date_filter'),
    path('tags_filter/<pk>', views.articles_tags_filter, name='articles_tags_filter'),
    path('author/<pk>', views.articles_author_filter, name='articles_author_filter'),
]
