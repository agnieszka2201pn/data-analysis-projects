p_k_n = input("Wybierz kamień, papier lub nożyce ")
print("Your choice is ", p_k_n)

import random
possible_choice = ["kamień", "papier", "nożyce"]
computer_choice = random.choice(possible_choice)
print("Computer's choice is: ", computer_choice)

if p_k_n == "kamień":
    if computer_choice == possible_choice[0]:
        print("remis")
    elif computer_choice == possible_choice[1]:
        print("you loose")
    else:
        print("you win")

if p_k_n == "papier":
    if computer_choice == possible_choice[0]:
        print("you win")
    elif computer_choice == possible_choice[1]:
        print("remis")
    else:
        print("you loose")

if p_k_n == "nożyce":
    if computer_choice == possible_choice[0]:
        print("you loose")
    elif computer_choice == possible_choice[1]:
        print("you win")
    else:
        print("remis")