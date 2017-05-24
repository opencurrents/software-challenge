from django.db import models

class Round(models.Model):
    current_round = models.IntegerField(default=1)      #Current round of game
    update = models.BooleanField(default=False)         #Indicate if game state has updated

class Player(models.Model):
    team = models.CharField(max_length=200)             #Player team
    current_choice = models.CharField(max_length=200)   #Most recent choice player has made
    score = models.FloatField(default=0,)               #Score of team