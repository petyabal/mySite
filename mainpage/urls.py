from django.urls import path
from . import views
 

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('your_own_game/', views.your_own_game, name='your_own_game'),
    path('interactive_crossword/', views.interactive_crossword, name='interactive_crossword'),
    path('phone_payments/', views.phone_payments, name='phone_payments'),
    path('dinnerware_accounting/', views.dinnerware_accounting, name='dinnerware_accounting'),
    path('world_war_ii/', views.world_war_ii, name='world_war_ii'),
    path('vacation_schedule/', views.vacation_schedule, name='vacation_schedule'),
    path('1C/', views.my1C, name='my1C'),
    path('inventory_accounting/', views.inventory_accounting, name='inventory_accounting'),
    path('contacts/', views.contacts, name='contacts'),
    path('achievements/', views.achievements, name='achievements'),
    path('<pk>/<note>', views.voting_for_programm, name='voting_for_programm')
]