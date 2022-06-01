"""
LESSON: 6.2 - Return Values
WARMUP 3
"""

import random

#### ------------------------------- ####
#### ---- GET GREETING FUNCTION ---- ####
#### ------------------------------- ####
def get_greeting():
    number = random.randint(1, 3)
    if number == 1:
        return "L BOZO"
    elif number == 2:
        return "L cope"
    elif number == 3:
        return "L skill issue"

#### ---------------------- ####
#### ---- MAIN PROGRAM ---- ####
#### ---------------------- ####
print(get_greeting())