from django.shortcuts import render

def main_page(request):
	return render(request, 'mainpage/main_page.html', {})

def your_own_game(request):
	return render(request, 'mainpage/your_own_game.html', {})

def interactive_crossword(request):
	return render(request, 'mainpage/interactive_crossword.html', {})

def phone_payments(request):
	return render(request, 'mainpage/phone_payments.html', {})

def dinnerware_accounting(request):
	return render(request, 'mainpage/dinnerware_accounting.html', {})

def world_war_ii(request):
	return render(request, 'mainpage/world_war_ii.html', {})

def vacation_schedule(request):
	return render(request, 'mainpage/vacation_schedule.html', {})

def contacts(request):
	return render(request, 'mainpage/contacts.html', {})

def achievements(request):
	return render(request, 'mainpage/achievements.html', {})
