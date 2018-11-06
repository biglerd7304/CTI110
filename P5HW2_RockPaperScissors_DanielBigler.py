# A game of Rock, Paper, Scissors
# 11-1-18
# CTI-110 P5HW2 - Rock, Paper, Scissors Game
# Daniel Bigler
#
import random
def main():
    print("type rock(1), paper(2), or scissors(3)")
    choice = int(input())
    # randomly generated number, 1 is rock, 2 is paper, 3 is scissors
    computer_choice = random.randint(1,3)
    #If player chooses rock
    if choice == 1:
        if computer_choice == 1:
            print("Computer chose rock, you tie")
        elif computer_choice == 2:
            print("Computer chose paper, you lose")
        else:
            print("Computer chose sissors, you win")
    #If player chooses paper
    elif choice == 2:
        if computer_choice == 1:
            print("Computer chose rock, you win")
        elif computer_choice == 2:
            print("Computer chose paper, you tie")
        else:
            print("Computer chose scissors, you lose")
    #If player chooses scissors
    else:
        if computer_choice == 1:
            print("Computer chose rock, you lose")
        elif computer_choice == 2:
            print("Computer chose paper, you win")
        else:
            print("Computer chose scissors, you tie")

main()
