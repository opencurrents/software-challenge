# coding: utf-8
#
# rps.py
#

"""
Author: Karthik B M

"""


import random          # imports the library named random

def rps():#Just rps
    """ this plays a game of rock-paper-scissors
        (or a variant of that game ...)
        inputs: no inputs    (prompted text doesn't count as input)
        outputs: no outputs  (printing doesn't count as output)
    """
    play = "yes"
    history_player1 = 0
    history_player2 = 0
    while play == "yes":
        #set player to True
        player1 = input("Player 1: Choose your weapon - \npress 1 for rock \npress 2 for paper \npress 3 for scissors?\n\n")
        player2 = input("Player 2: Choose your weapon - \npress 1 for rock \npress 2 for paper \npress 3 for scissors?\n\n")
        if player1 == player2:
            if player1=="1":
                print("Player 1 chose Rock")
                print("Player 2 chose Rock")
            elif player1=="2":
                print("Player 1 chose Paper")
                print("Player 2 chose Paper")
            else:
                print("Player 1 chose Scissor")
                print("Player 2 chose Scissor")
            
            print("Tie! dude we both selected same one")
            print("\n\nIT'S A TIE\n\n")
            history_player2 += 0.5
            history_player1 += 0.5
        elif player1 == "1":
            if player2 == "2":
                print("Player 1 chose rock")
                print("Player 2 chose paper")
                print("Player 2 says...I won it you loser. Paper covers Rock")
                print("\n\nPLAYER 2 WINS\n\n")
                history_player2 += 1
            else:
                print("Player 1 chose Rock")
                print("Player 2 chose Scissor")
                print("Player 2 says... Seriously man :( you are becoming good at it. you win. Rock smashes Scissors")
                print("\n\nPLAYER 1 WINS\n\n")
                history_player1 += 1
        elif player1 == "2":
            if player2 == "3":
                print("Player 1 chose Paper")
                print("Player 2 chose Scissor")
                print("Player 1 says... Doh! lucky you won again. Scissors cut Paper.")
                print("\n\nPLAYER 2 WINS\n\n")
                history_player2 += 1
            else:
                print("Player 1 chose Paper")
                print("Player 2 chose Rock")
                print("Player 1 says... Bring it on. I won!!  Paper covers Rock")
                print("\n\nPLAYER 1 WINS\n\n")
                history_player1 += 1
        elif player1 == "3":
            if player2 == "1":
                print("Player 1 chose Scissors")
                print("Player 2 chose Rock")
                print("Player 2 says... Oohahaha you go down matey. Rock smashes Scissors. Booom!!")
                print("\n\nPLAYER 2 WINS\n\n")
                history_player2 += 1
            else:
                print("Player 1 chose Scissor")
                print("Player 2 chose Paper")
                print("Player 1 says...You loser :D!! Scissors cut Paper")
                print("\n\nPLAYER 1 WINS\n\n")
                history_player1 += 1
        else:
            print("That's not a valid play. Check your spelling!")
        print("\n\n\n++++++++++++++++++++++++++++++++\nPlayer 1 points: ",str(history_player1))
        print("Player 2 points: ",str(history_player2),"\n++++++++++++++++++++++++++++++++\n")
        play = input("play: yes or no? \n")
        if play=="yes" or play=="no":
            if play=="no":
                print("Exiting RPS....\nEntering 'Rock Paper Scissor Lizard Spock'... This will be a single player game with computer as your opponent\n")
            continue
        else:
            print("Oops wrong entry !!I'm outta here\n You will enter my brother 'Rock Paper Scissor Lizard Spock' now ")



def rpsls():#RPS 5
    '''
    Runs the RPSLS game with an algorithm I found on net. it applies a formula which can be applied ie..

    (computer_select - player_select)%(total number of selections)
    P.S: the selections must be assigned to number in a order to apply the formula

    after that if the answer is greater than {(total number of selections)+1}/2 then player wins else computer wins

    '''
    rpsls_list = ["rock","spock","paper","lizard","scissors"]
    play="yes"
    while play=="yes":
        player_guess = str(input('Enter your choice.. Options: rock, spock, paper, lizard, scissors\n'))
        if player_guess=='' or player_guess not in rpsls_list:
            print("Enter a valid choice !!")
            break
        player_number = rpsls_list.index(player_guess)
        comp_number = random.randrange(0,5)
        winner = (comp_number - player_number) % 5
        if winner < 3:
            player_win = False
        else:
            player_win = True
        comp_name = rpsls_list[comp_number]
        print ("You choose " + str(player_guess))
        print ("I chose " + comp_name)
        if player_win:
            print ("Darn it. You win!\n")
        elif comp_number == player_number:
            print ("There you go a tie bro!\n")
        else:
            print ("K.O I win :D !\n")
        play = input("play: yes or no? \n")
        if play=="yes" or play=="no":
            if play=="no":
                print("Exiting 'Rock Paper Scissor Lizard Spock'.....\nEntering RPS-25... ")
            continue
        else:
            print("Oops wrong entry !!I'm outta here\n You will enter my BIG brother RPS-25 now ")

def rps_25():#RPS 25
    """Works perfect with the same algorithm"""
    objects=["gun", "dynamite", "nuke", "lightning", "devil", "dragon", "alien", "water", "bowl", "air"\
    , "moon", "paper", "paper", "sponge", "wolf", "cockroach", "tree", "man", "woman", "monkey", "snake"\
    , "axe", "scissors", "fire", "sun", "rock"]
    play="yes"
    while play=="yes":
        player_guess = str(input('Enter your choice.. Options: \n%s \n' %'\n'.join(objects)))
        if player_guess=='' or player_guess not in rpsls_list:
            print("Enter a valid choice bruh!!")
            break
        player_number = objects.index(player_guess)
        comp_number = random.randrange(0,25)
        winner = (comp_number - player_number) % 25
        if winner < 13:
            player_win = False
        else:
            player_win = True
        comp_name = objects[comp_number]
        print ("You choose " + str(player_guess))
        print ("I chose " + comp_name)
        if player_win:
            print ("Pfft you getting better playing with my computer brothers. You win!\n")
        elif comp_number == player_number:
            print ("I can't do much it's a TIEEEE!!\n")
        else:
            print ("You can't beat me loser xD. I win\n")
        if play=="yes" or play=="no":
            if play=="no":
                print("Exiting RPS-25.....\nEntering RPS-101... ")
            continue
        else:
            print("Oops wrong entry bruh!!I'm outta here\n You will enter my MONSTER brother RPS-101 now ")


def rps_101():#RPS 101
    rps_101 = ["dynamite","tornado","quicksand","pit","chain","gun","law","whip","sword","rock","death","wall","sun"\
    ,"camera","fire","chainsaw","school","scissors","poison","cage","axe","peace","computer","castle","snake","blood"\
    ,"porcupine","vulture","monkey","king","queen","prince","princess","police","woman","baby","man","home","train","car"\
    ,"noise","bicycle","tree","turnip","duck","wolf","cat","bird","fish","spider","cockroach","brain","community","cross"\
    ,"money","vampire","sponge","church","butter","book","paper","cloud","airplane","moon","grass","film","toilet","air"\
    ,"planet","guitar","bowl","cup","beer","rain","water","tv","rainbow","ufo","alien","prayer","mountain","satan","dragon"\
    ,"diamond","platinum","gold","devil","fence","videogame","math","robot","heart","electricity","lightning","medusa","power"\
    ,"laser","nuke","sky","tank","helicopter"]
    play="yes"
    while play=="yes":
        player_guess = str(input('Enter your choice.. Options: \n%s \n' %'\n'.join(rps_101)))
        if player_guess=='' or player_guess not in rpsls_list:
            print("Enter a valid choice bruh!!")
            break
        player_number = rps_101.index(player_guess)
        comp_number = random.randrange(0,101)
        winner = (comp_number - player_number) % 101
        if winner < 51:
            player_win = False
        else:
            player_win = True
        comp_name = rps_101[comp_number]
        print ("You choose " + str(player_guess))
        print ("I chose " + comp_name)
        if player_win:
            print ("Darn it. You win!\n")
        elif comp_number == player_number:
            print ("There you go a tie bro!\n")
        else:
            print ("K.O I win :D !\n")
        if play=="yes" or play=="no":
            if play=="no":
                print("Exiting RPS-101.....\nEntering Real world... ")
            continue
        else:
            print("Oops wrong entry bruh!!I'm outta here\n Finally you are free enjoy :) ")

if __name__=="__main__":
    rps()
    rpsls_input = input("Do you want to play Rock, Paper, Scissor, Lizard and Spock? yes or no\n")
    if rpsls_input == "yes":
        rpsls()
    else:
        rps_25_input = input("Do you want to play RPS_25? yes or no\n")
        if rps_25_input == "yes":
            rps_25()
        else:
            rps_101_input = input("Do you want to play RPS_101? yes or no\n")
            if rps_101_input == "yes":
                rps_101()
            else:
                print("Cya Later buddy!!")

