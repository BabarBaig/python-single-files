# Rock-paper-scissors-lizard-Spock template
import random

# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions

def number_to_name(number):
    # Receive a number 0..4 and return corresponding name
    if number   == 0:
        return "rock"
    elif number == 1:
        return "Spock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "lizard"
    elif number == 4:
        return "scissors"
    else:
        print "Sorry I don't recognize: ", number
        return -1
    
def name_to_number(name):
    # Receive a name and return a corresponding number 0..4
    if name   == "rock":
        return 0
    elif name == "Spock":
        return 1
    elif name == "paper":
        return 2
    elif name == "lizard":
        return 3
    elif name == "scissors":
        return 4
    else:
        print "Sorry I don't recognize: ", name
        return -1


def rpsls(name):
    # convert name to player_number using name_to_number
    player_number = name_to_number(name)

    # compute random guess for comp_number using random.randrange()
    comp_number = random.randrange(0, 5)

    # compute difference of player_number and comp_number modulo five
    result = ((player_number - comp_number) + 5) % 5

    # use if/elif/else to determine winner
    if   result == 0:
        print_result = "Player and computer tie!"
    elif result < 3:
        print_result = "Player wins!"
    else:
        print_result = "Computer wins!"

    # convert comp_number to name using number_to_name
    comp_choice = number_to_name(comp_number)
    
    # print results
    print "\n"
    print "Player chooses"  , name
    print "Computer chooses", comp_choice
    print print_result

    
# test your code
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric


