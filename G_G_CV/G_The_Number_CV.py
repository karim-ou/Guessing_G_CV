import random
import time

name = input("what's your name : ")
# the player will chose the high number in the range
low = 1
try:
    high = int(input(f"{name} chose a number : "))
except ValueError:
    print("you did not enter a number, try again!")
    quit()
# intro 
print(f"Well {name}, guess a number between 1 and {high}, and i will guess it!")
# the program will stop for 4s for the player to be ready 
time.sleep(4)
feedback = ""
feedback_limit = 5
feedback_count = 0
out_of_guesses = False

while feedback != "c" and low != high and not(out_of_guesses):
    guess = random.randint(low, high)
    # keep track of feedbacks the player will give
    try:
        if feedback_count < feedback_limit:
            feedback = str(input(f"is {guess} too low (L), too high (H), or correct(C) : ")).lower()
            feedback_count += 1
            # here we will change the range based on the player feedback 
            if feedback == "h":
                high = guess - 1
            elif feedback == "l":
                low = guess + 1
            elif feedback == "c":
                pass
            else: raise ValueError
        else:
            out_of_guesses = True

    except ValueError:
        print("You did not give a feedback , try again")
        quit()
# the program win!
if feedback == "c" :
    print(f"Yay! i guessed your number {guess} correctly! in {str(feedback_count)} guesses !")
# the program lose :(
else:
    print (":( i'm out of guesses , you win!!")
    
