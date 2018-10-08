from django.template import *
from django.http import *
from django.shortcuts import *
from .models import *
from operator import itemgetter

def index(request):
	return render(request,'index.html')

def leaderboard(request):
	result = Result.objects.all()
	lead=dict()
	for res in result:
		if(res.team.Team_Name in lead):
			lead[res.team.Team_Name]+=1
		else:
			lead[res.team.Team_Name]=1
	sorted_teams = list(reversed(sorted(lead.items(), key=itemgetter(1))))
	return render(request,'leaderboard.html', {'teams': sorted_teams})

def team_list(request):
	teams = Team.objects.all()
	return render(request,'team_list.html', {'team_list': teams})

def team_details(request, team_id):
	team = Team.objects.get(pk=team_id)
	return render(request, 'team_details.html', {'team': team})

def games(request):
	games = Game.objects.order_by('pk').reverse()
	return render(request, 'games.html', {'games': games})

def instructions(request):
	return render(request,'instructions.html')
