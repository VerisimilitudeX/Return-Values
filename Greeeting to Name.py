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

    done = input("Type a number 1 - 5 or done: ")
    if done == "done":
        break

    greeting = get_greeting(int(done))
    print(name + ", " + greeting + "!")
