answer = input("Type your name: ")
print("Wecome", answer, "to this adventure!")

answer = input("You are on a dirt road in the middle of nowhere, at a junction where you have to choose to go left or right. Which way would you like to go? ").lower()

if answer== "left":
    answer = input("You've come to a river, you can either walk around it or swim accross: ")
    
    if answer == "swim":
        print("Oh no, there's a crocodile. You die :( ")
    elif answer == "walk":
        print("Oops! that's a wrong turn. Time out")
    else:
        print("Not a valid option. You lose")

elif answer == "right":
    answer = input("You choose the right way (pun unintended whew). You have two choices, walk or run to the finish line? ")

    if answer == "walk":
        print("Oh no, you were timed out. You lose :( ")
    elif answer == "run":
        print("Yey! you win the shortest time to finish the adventure!.")
    else:
        print("Not a valid option. You lose")
else:
    print("Not a valid option. You lose.")
