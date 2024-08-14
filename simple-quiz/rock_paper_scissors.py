import random

user_wins = 0
computer_wins = 0
list_of_options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type Rock/Paper/Scissors or Q for quit: ").lower()
    # islower converts all in the input letters to lower caps
    if user_input == "q":
        break

    if user_input not in list_of_options:
        continue

    random_number = random.randint(0, 2)
    # rock = 0, paper = 1, scissors = 2
    computer_pick = list_of_options[random_number]
    print("The computer picked", computer_pick + ".")

    if user_input == "rock" and computer_pick == "scissors":
        print("You won!")
        user_wins += 1

    elif user_input == "paper" and computer_pick == "rock":
        print("you won!")
        user_wins += 1

    elif user_input == "scissors" and computer_pick == "paper":
        print("you won!")
        user_wins += 1

    else:
        print("You lost :(")
        computer_wins += 1

print("You won", user_wins, "times.")
print("The computer won", computer_wins, "times.")
print("Goodbye!")
