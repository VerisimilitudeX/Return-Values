"""
LESSON: 6.2 - Return Values
WARMUP 2
"""

#### -------------------------------- ####
#### ---- DOUBLE NUMBER FUNCTION ---- ####
#### -------------------------------- ####
def double_number(num):
    return num * 2

#### ---------------------- ####
#### ---- MAIN PROGRAM ---- ####
#### ---------------------- ####
num = int(input("Enter a number: "))
double = double_number(num)
print("That number doubled is: " + str(double))