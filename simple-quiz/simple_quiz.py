print("Welcome to my Cool Quiz! ;)")

playing = input("Do you want to play? ")
score = 0

if playing != "yes": # if True then quit
    quit()
print("Great let's begin!")

answer = input("What is the meaning of CPU? ")

if answer == ("Central Processing Unit"):
    print("Well done! :)")
    score += 1
else:
    print("sheesh! try again")

answer = input("What is the meaning of GPU? ")

if answer == ("graphics processing unit"):
    print("Amazing!")
    score += 1
else:
    print("Try again :(")

answer = input("What is the meaning of DB? ")

if answer == ("DataBase"):
    print("Correct!")
    score += 1
else:
    print("Incorrect")

answer = input("What does RAM stand for? ")

if answer == ("Random-access memory"):
    print("Correct!")
    score += 1
else:
    print("Incorrect")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 4) * 100) + "%.")

total_score = input(score / 4 * 100)
if total_score == (score / 4 * 100):
    print("Congratulations!! You are a a Genius! ;)")
else:
    print("Better Luck Next time!")
