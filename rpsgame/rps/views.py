from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Player, Round
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse
import json

def select(request):

    #Create db entries if needed
    try:
        red_player = Player.objects.get(team="Red")
        blue_player = Player.objects.get(team="Blue")
        round = Round.objects.get(id=1)
    except ObjectDoesNotExist:
        red_player = Player(team="Red",current_choice="None")
        red_player.save()
        blue_player = Player(team="Blue", current_choice="None")
        blue_player.save()
        round = Round(update=False)
        round.save()

    #New round, increment round and reset choices
    if red_player.current_choice != "None" and blue_player.current_choice != "None":
        round.current_round = round.current_round + 1
        red_player.current_choice = "None"
        blue_player.current_choice = "None"
        round.save()
        red_player.save()
        blue_player.save()

    context = {'red_player':red_player, 'blue_player':blue_player, 'round':round}
    return render(request, 'rps/select.html', context)

#Handles selections made from selection page
def submit(request):
    if request.method == 'POST':
        red_player = Player.objects.get(team="Red")
        blue_player = Player.objects.get(team="Blue")
        round = Round.objects.get(id=1)

        #Reset all persistent values
        if "reset" in request.POST:
            round.current_round = 1
            red_player.current_choice = "None"
            red_player.score = 0
            blue_player.current_choice = "None"
            blue_player.score = 0
            round.update = True
            round.save()
            red_player.save()
            blue_player.save()

            return HttpResponseRedirect(reverse('select'))

        #The following logic blocks are for saving the user choice to the db and incrementing score
        #if both players have submitted a choice
        if "red_rock" in request.POST:
            red_player.current_choice = "Rock"
        elif "red_paper" in request.POST:
            red_player.current_choice = "Paper"
        elif "red_scissors" in request.POST:
            red_player.current_choice = "Scissors"
        elif "blue_rock" in request.POST:
            blue_player.current_choice = "Rock"
        elif "blue_paper" in request.POST:
            blue_player.current_choice = "Paper"
        elif "blue_scissors" in request.POST:
            blue_player.current_choice = "Scissors"

        #Game ends in a tie, update scores
        if red_player.current_choice == blue_player.current_choice:
            red_player.score = red_player.score + 0.5
            blue_player.score = blue_player.score + 0.5
            round.update = True

        #Game ends with a winner, update score
        elif (red_player.current_choice == "Rock" and blue_player.current_choice == "Scissors") or (red_player.current_choice == "Paper" and blue_player.current_choice == "Rock") or (red_player.current_choice == "Scissors" and blue_player.current_choice == "Paper"):
            red_player.score = red_player.score + 1
            round.update = True
        elif (blue_player.current_choice == "Rock" and red_player.current_choice == "Scissors") or (blue_player.current_choice == "Paper" and red_player.current_choice == "Rock") or (blue_player.current_choice == "Scissors" and red_player.current_choice == "Paper"):
            blue_player.score = blue_player.score + 1
            round.update = True
        blue_player.save()
        red_player.save()
        round.save()

    return HttpResponseRedirect(reverse('results'))

#Fill results page template
def results(request):
    red_player = Player.objects.get(team="Red")
    blue_player = Player.objects.get(team="Blue")
    round = Round.objects.get(id=1)
    context = {'red_player': red_player, 'blue_player': blue_player, 'round': round}
    return render(request, 'rps/results.html', context)

#Used for ajax refreshing of pages. Checks to see if the game state has been updated
def refresh(request):
    if request.method == 'GET':
        round = Round.objects.get(id=1)
        data = {}
        if round.update:
            data['update'] = True
            round.update = False
        else:
            data['update'] = False
        round.save()
        return HttpResponse(json.dumps(data), content_type="application/json")
    else:
        return HttpResponse("Not a GET request")