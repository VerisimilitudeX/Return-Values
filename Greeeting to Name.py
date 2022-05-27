"""
LESSON: 6.2 - Return Values
TECHNIQUE 1: Mapping Function
PRACTICE 1
"""

#### ---- LIBRARIES ---- ####
import random

#### ------------------------------- ####
#### ---- GET GREETING FUNCTION ---- ####
#### ------------------------------- ####
def get_greeting(num):
    if num == 0:
        return "hello"
    elif num == 1:
        return "hi"
    elif num == 2:
        return "lbozo"
    elif num == 3:
        return "hola"
    elif num == 4:
        return "como estas"

#### ---------------------- ####
#### ---- MAIN PROGRAM ---- ####
#### ---------------------- ####
name = input("What is your name? ")

done = ""
while done != "done":

    # Get input from the user
    done = input("Type a number 1 - 5 or done: ")
    if done == "done":
        break

    # Get a greeting based on the user's entered value
    greeting = get_greeting(int(done))
    print(name + ", " + greeting + "!")

    # Print the greeting
    


# Turn in your Coding Exercise.
