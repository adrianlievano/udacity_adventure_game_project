import time
import random

#This function prints messages to the user
def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(1)

#This function checks if the user has the key item to win
def item_check(items):
    flag = 0
    if ("Sword of Ogoroth" in items):
        flag = 1
        return flag
    else:
        return flag

#This function stops or restarts the game
def restart_game():
    restart_var = input("Would you like to play again? (y/n)")
    if (restart_var == 'y'):
        play_game()
    elif (restart_var == 'n'):
        print_pause("Thanks for playing! See you next time.")

#This function checks if the user will knock of peer into the cave throughout the game
def knock_or_peer_check(items):
    ##Code to refactor
    print_pause(" ")
    print_pause("Enter 1 to knock on the door of the house")
    print_pause("Enter 2 to peer into the cave.")
    print_pause("What would you like to do?")
    reply = input("(Please enter 1 or 2.)\n")
    flag = item_check(items)
    #if user peers into cave again and has the sword

    if (reply == '2' and flag == 0):
        print_pause("You peer cautiously into the cave.")
        print_pause("It turns out to be only a very small cave.")
        print_pause("Your eye catches a glint of metal behind a rock.")
        print_pause("You have found the magical Sword of Ogoroth!")
        print_pause("You discard your silly old dagger and take the sword with you.")
        print_pause("You walk back out to the field.")
        items.append("Sword of Ogoroth")
        knock_or_peer_check(items)

    elif (reply == '2' and flag == 1):
        print_pause("You peer cautiously into the cave.")
        print_pause("You've been here before, and gotten all the good stuff. It's just an empty cave now.")
        print_pause("You walk back out to the field.")
        knock_or_peer_check(items)

    return reply

def fight_or_run_check(animal, reply, items):
    print_pause("You approach the door of the house.")
    print_pause("You are about to knock when the door opens and out steps a " + animal)
    print_pause("Eep! This is the " + animal + "'s" + " house!")
    print_pause("The " + animal +  " attacks you!")
    flag = item_check(items)

    if (reply == '1' and flag == 1):
        print_pause("As the wicked " + animal + " moves to attack, you unsheath your new sword.")
        print_pause("The Sword of Ogoroth shines brightly in your hand as you brace yourself for the attack.")
        print_pause("But the wicked " + animal + " takes one look at your shiny new toy and runs away!")
        print_pause("You have rid the town of the wicked " + animal + " You are victorious!")
        break

    elif ((reply == '1' and flag == 0)):
        print_pause("You feel a bit under-prepared for this, what with only having a tiny dagger.")
        reply = input("Would you like to (1) fight or (2) run away?")

        if (reply == '1'):
            print_pause("You do your best...")
            print_pause("but your dagger is no match for the " + animal)
            print_pause("You have been defeated!")
            restart_game()

        elif (reply == '2'):
            print_pause("You run back into the field. Luckily, you don't seem to have been followed.")
            knock_or_peer_check(items)


#This function runs the adventure game from start to finish
def play_game():
    items = []
    animal_bases = ["dragon", "fairie", "gorgon"]
    animal = random.choice(animal_bases)
    print_pause("You find yourself standing in an open field, filled with grass and yellow wildflowers.")
    print_pause("Rumor has it that a " + animal + " is somewhere around here, and has been terrifying the nearby village." )
    print_pause("In front of you is a dark house.")
    print_pause("To your right is a dark cave.")
    items.append('dagger')

    while True:
        reply = knock_or_peer_check(items)
        fight_or_run_check(animal, reply, items)
        #reply = knock_or_peer_check(items)

    #need to run in a loop unil it wins

#Initialize Game

play_game()
