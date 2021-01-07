import random
import time

name = input("what's your name : ")

low = 1
try:
    high = int(input(f"{name} chose a number : "))
except ValueError:
    print("you did not enter a number, try again!")
    quit()

print(f"Well {name}, guess a number between 1 and {high}, and i will guess it!")

time.sleep(4)
feedback = ""
feedback_limit = 5
feedback_count = 0
out_of_guesses = False

while feedback != "c" and low != high and not(out_of_guesses):
    guess = random.randint(low, high)
    try:
        if feedback_count < feedback_limit:
            feedback = str(input(f"is {guess} too low (L), too high (H), or correct(C) : ")).lower()
            feedback_count += 1
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

if feedback == "c" :
    print(f"Yay! i guessed your number {guess} correctly! in {str(feedback_count)} guesses !")
else:
    print (":( i'm out of guesses , you win!!")