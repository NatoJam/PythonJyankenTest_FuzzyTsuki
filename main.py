# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random
from thefuzz import fuzz, process

def senteGote():
    saikoro = [1, 2, 3, 4, 5, 6]
    a = random.choices(saikoro)
    b = random.choices(saikoro)
    while (a == b):
        a = random.choices(saikoro)
        b = random.choices(saikoro)
    if (a > b):
        order = "Sente"
    else:
        order = "Gote"
    return order


def jyanken():
    case = ["rock", "scissors", "paper"]
    cpu_choice = random.choices(case)
    return cpu_choice


def toFuzz(player):
    str1 = "rock"
    str2 = "scissors"
    str3 = "paper"
    fz1 = int(fuzz.ratio(player, str1))
    fz2 = int(fuzz.ratio(player, str2))
    fz3 = int(fuzz.ratio(player, str3))
    if (fz1 >= 60):
        return str1
    elif (fz2 >= 60):
        return str2
    elif (fz3 >= 60):
        return str3
    else:
        print("Wrong input. Try again.")
        return "err"


def game():
    order = senteGote()
    if (order == "Sente"):
        player = input("Please input your choice.\n")
        npc = jyanken()
        print("Your opponent selected: " + str(npc))
    elif (order == "Gote"):
        npc = jyanken()
        print("Your opponent selected: " + str(npc))
        player = input("Please input your choice.(rock,scissors,paper)\n")

    play = toFuzz(player)
    print("Your choice is: " + play)
    npc = "".join(npc)

    if (play == "rock" and npc == "scissors"):
        print("You Win")
    elif (play == "rock" and npc == "paper"):
        print("You Lose")
    elif (play == "rock" and npc == "rock"):
        print("Hikiwake")
    elif (play == "scissors" and npc == "rock"):
        print("You Lose")
    elif (play == "scissors" and npc == "scissors"):
        print("Hikiwake")
    elif (play == "scissors" and npc == "paper"):
        print("You Win")
    elif (play == "paper" and npc == "rock"):
        print("You Win")
    elif (play == "paper" and npc == "scissors"):
        print("You Lose")
    elif (play == "paper" and npc == "paper"):
        print("Hikiwake")
    elif (play == "err"):
        game()


def trigger():
    inp = input("Shall we start the Jyanken Game?(y/n)\n")
    if (inp == "Y" or inp == "y"):
        game()
    elif (inp == "N" or inp == "n"):
        print("Have a nice day.\n")
    else:
        print("Wrong input. Try again.\n")
        trigger()


trigger()
