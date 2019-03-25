from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Player
from .forms import PlayerForm
import requests
import json

def index(request):

    # URL returns information about every Buffalo Sabre ever
    allSabresURL = 'http://www.nhl.com/stats/rest/skaters?isAggregate=true&reportType=basic&isGame=false&reportName=skatersummary&sort=[{%22property%22:%22points%22,%22direction%22:%22DESC%22},{%22property%22:%22goals%22,%22direction%22:%22DESC%22},{%22property%22:%22assists%22,%22direction%22:%22DESC%22}]&factCayenneExp=gamesPlayed%3E=1&cayenneExp=gameTypeId=2%20and%20seasonId%3E=19171918%20and%20seasonId%3C=20182019%20and%20teamId=7'
    allSabres = requests.get(allSabresURL).json()

    allSabresList = []

    # Converting JSON data to list of dictionaries (dictionary represents a player)
    for player in allSabres['data']:
        tempDict = {
            'id' : player['playerId'],
            'fullName' : player['playerName'],
            'position' : player['playerPositionCode'],
            'points' : player['points'],
            'goals' : player['goals'],
            'assists' : player['assists']
        }
        allSabresList.append(tempDict)

    # Getting all players added to the database table by the user's searches

    if request.method == 'POST':
        form = PlayerForm(request.POST)
        form.save()
    
    form = PlayerForm()

    players = Player.objects.all()
    searchedPlayersList = []

    for x in players:
        searchedPlayer = next((player for player in allSabresList if player['fullName'] == x.fullName), None)
        #print(searchedPlayer['fullName']) 
        searchedPlayersList.append(searchedPlayer)
    
    print(searchedPlayersList)

    context = {'searchedPlayersList' : searchedPlayersList, 'form' : form}

    return render(request, 'hockeyGraphs/index.html', context)
