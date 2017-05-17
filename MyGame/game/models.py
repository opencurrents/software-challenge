from django.db import models

# Create your models here.
class Board (models.Model):
    output = models.CharField(max_length=9,default = " " * 9)

    # player_x = models.CharField(max_length=64)
    # player_x = models.CharField(max_length=64)
