from curses.ascii import HT
import re
from django.shortcuts import HttpResponse, render
from .models import*
import pandas as pd
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
# from asyncio.windows_events import NULL

# Create your views here.

def index(request):
    cap_space=20000
    return render(request, 'fantasyPage.html', {'cap_space':cap_space, 'player_count': 10})

def addPlayer(request):
    item = fanPlayer.objects.all().values()
    df = pd.DataFrame(item)
    playerName = request.POST.get('playerName_')
    player = df[df['name']==playerName]
    team_ = team.objects.all().values() 
    team_df=pd.DataFrame(team_)
    player_already_on_team=False
    if team.objects.filter(name=playerName).exists():
        print("player exists already")
        player_already_on_team=True
    
    if player.empty or player_already_on_team==True:
        #can't add the player, invalid name
        print(1)
        cap_space = 20000-team_df['salary'].sum()
        player_count = 10-len(team_df)
        return render(request, 'fantasyPage.html', {'team_':team_, 'cap_space':cap_space, 'player_count':player_count})
    else:
        done=False
        if len(team_df)!=0:
            curr_cap = 20000-team_df['salary'].sum()
            if curr_cap<=0:
                done=True
                team.objects.all().delete()
                cap_space=20000
                return render(request, 'fantasyPage.html', {'cap_space':cap_space, 'player_count': 10})
        if done==False:
            new_entry = team(name=playerName,age=player['age'],scoring_grade=player['scoring_grade'],passing_grade=player['passing_grade'],rebounding_grade=player['rebounding_grade'],rating=player['rating'],efficiency=player['efficiency'],turnover_grade=player['turnover_grade'],overall=player['overall'],salary=player['salary'])
            new_entry.save()
            team__ = team.objects.all().values() 
            team_df_=pd.DataFrame(team__)
            cap_space = 20000-team_df_['salary'].sum()
            player_count = 10-len(team_df_)
            return render(request, 'fantasyPage.html', {'team_':team__,'cap_space':cap_space, 'player_count':player_count})

def submit_team(request):
    team_ = team.objects.all().values() 
    team_df=pd.DataFrame(team_)
    cap_space = 20000-team_df['salary'].sum()
    team_overall = team_df['overall'].mean()
    team_age = team_df['age'].mean()
    team_scoring = team_df['scoring_grade'].mean()
    team_passing = team_df['passing_grade'].mean()
    team_rebounding = team_df['rebounding_grade'].mean()
    team_rtg = team_df['rating'].mean()
    team_eff = team_df['efficiency'].mean()
    team_turnOver = team_df['turnover_grade'].mean()
    total_cap = team_df['salary'].sum()
    team_name__ = request.POST.get('teamName_')
    team.objects.all().delete()
    new_team = user_created_teams(team_name=team_name__,mean_age=team_age, mean_scoring=team_scoring, mean_passing=team_passing, mean_rebounding=team_rebounding, mean_rating=team_rtg, mean_efficiency=team_eff, 
    mean_turnOver_grade=team_turnOver,mean_overall=team_overall,total_spendings=total_cap)
    new_team.save()
    return render(request, 'teamReport.html', {'team_name':team_name__,'team_':team_, 'cap_space':cap_space,
    'team_overall':team_overall,'team_age':team_age,'team_scoring':team_scoring,'team_passing':team_passing,
    'team_rebounding':team_rebounding,'team_rtg':team_rtg,'team_eff':team_eff,'team_turnOver':team_turnOver, 'total_cap':total_cap})

def leaderboard(request):
    user_created_teams.objects.all().order_by('mean_overall')
    team_ = user_created_teams.objects.all()
    return render(request, 'leaderboard.html', {'team_': team_})