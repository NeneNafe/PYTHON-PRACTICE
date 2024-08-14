import random
# random gets any random number within a specified range

top_of_range = input("Type a number: ")

if top_of_range.isdigit(): # converting the string to an integer
    top_of_range = int(top_of_range)

    if top_of_range <= 0: # Checks if the number typed is greater than 0
        print("Type a number greater than 0 next time!")
        quit()
else:
    print("Please type a number next time!")
    quit()

random_number = random.randint(0, top_of_range) # generates diferent random numbers
total_guesses = 0

while True:
    total_guesses += 1
    users_guess = input("Make a guess: ")
    if users_guess.isdigit():
        users_guess = int(users_guess)
    else:
        print("Guess a number next time!")
        continue

    if users_guess == random_number:
        print("You guessed correct!")
        break
    elif users_guess > random_number:
        print("you guessed above the number!")
    else:
        print("You guessed below the number!")

print("You got", total_guesses, "guesses correct!")
