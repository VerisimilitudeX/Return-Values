"""
LESSON: 6.2 - Return Values
EXERCISE: Gremlin Grower
"""

#### ---- LIBRARIES ---- ####
import random


#### ------------------------------ ####
#### ---- RANDOM NAME FUNCTION ---- ####
#### ------------------------------ ####

# DEFINE the random_name function
def random_name():

    # Create a list called caps containing all non-vowel
    # capital letters as strings
    caps = ["B", "C", "D", "J", "F", "G", "H", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "V", "W", "X", "Y", "Z"]

    # Create a list called vowels containing all
    # lower-case vowels
    vowels = ["a", "e", "i", "o", "u"]

    # Create a list called consonants containing all
    # lower-case non-vowels
    consonants = ["b", "c", "d", "j", "f", "g", "h", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]

    # Create a variable called name and assign it a
    # value from caps at an index that is a random
    # number between 0 and the length of caps - 1
    name = caps[random.randint(0, len(caps) - 1)]

    # Create a variable length that holds a random
    # number between 3 and 10
    length = random.randint(3, 10)

    # For i in a range of the length variable
    for i in range(length):

        # If i mod 3 is 0
        if (i % 3) == 0:

            # Increment name by an item from vowels list,
            # at a random index between 0 and the length
            # of vowels - 1
            name += vowels[random.randint(0, len(vowels) - 1)]

        # Else
        else:

            # Increment name by an item from consonants
            # list, at a random index between 0
            # and the length of consonants - 1
            name += consonants[random.randint(0, len(consonants) - 1)]

    # RETURN the name variable
    # ---> TEST AFTER THIS LINE <--- #
    return name

#### --------------------------- ####
#### ---- GET MOOD FUNCTION ---- ####
#### --------------------------- ####

# DEFINE the get_mood function with PARAMETER
# mood_number
def get_mood(mood_number):

    # If mood_number is -3
    if mood_number == -3:

        # RETURN string " is somewhat annoyed."
        return " is somewhat annoyed."

    # Else if mood_number is -2
    elif mood_number == -2:

        # RETURN string " is grumpy because it hasn't slept."
        return " is grumpy because it hasn't slept."

    # Else if mood_number is -1
    elif mood_number == -1:

        # RETURN string " is stressed out."
        return " is stressed out."

    # Else if mood_number is 0
    elif mood_number == 0:

        # RETURN string " is bored."
        return " is bored."

    # Else if mood_number is 1
    elif mood_number == 1:

        # RETURN string " is excited to see you."
        return " is excited to see you."

    # Else if mood_number is 2
    elif mood_number == 2:

        # RETURN string " is inspired and wants to make something."
        return " is inspired and wants to make something."

    # Else if mood_number is 3
    elif mood_number == 3:

        # RETURN string " is feeling confident."
        # ---> TEST AFTER THIS LINE <--- #
        return " is feeling confident."

#### ----------------------------- ####
#### ---- GET ADVICE FUNCTION ---- ####
#### ----------------------------- ####

# DEFINE get_advice function with PARAMETER mood_number
def get_advice(mood_number):

    # If mood_number is less than 0
    if mood_number < 0:

        # Set bad_mood to a random integer between 1
        # and 3
        bad_mood = random.randint(1, 3)

        # If bad_mood is 1
        if bad_mood == 1:

            # RETURN string "Eh, whatever."
            return "Eh, whatever."

        # Else if bad_mood is 2
        elif bad_mood == 2:

            # RETURN string "I don't care."
            return "I don't care."

        # Else if bad_mood is 3
        elif bad_mood == 3:

            # RETURN string "I don't have time for this."
            # ---> TEST AFTER THIS LINE <--- #
            return "I don't have time for this."

    # Else if mood_number is greater than 0
    elif mood_number > 0:

        # Set good_mood to a random integer between 1
        # and 3
        good_mood = random.randint(1, 3)

        # If good_mood is 1
        if good_mood == 1:

            # RETURN string "I believe in you!"
            return "I believe in you!"

        # Else if good_mood is 2
        elif good_mood == 2:

            # RETURN string "Everything will be okay."
            return "Everything will be okay."

        # Else if good_mood is 3
        elif good_mood == 3:

            # RETURN string "Face your problems with calm confidence."
            # ---> TEST AFTER THIS LINE <--- #
            return "Face your problems with calm confidence."

    # Else
    else:

        # RETURN string "Huh? I wasn't paying attention."
        # ---> TEST AFTER THIS LINE <--- #
        return "Huh? I wasn't paying attention."

#### ---------------------- ####
#### ---- MAIN PROGRAM ---- ####
#### ---------------------- ####

# --- Variables --- #
name = ""
mood = 0

#### ---- MAIN LOOP ---- ####
done = False
while not done:


    #### ---- MENU ---- ####
    print()
    print("---- MENU ----")
    print()

    if name == "":
        print("You have no gremlin.")
    else:
        print("You have a gremlin named " + name)

        # Create a variable mood_string and assign it
        # to a CALL of the get_mood function with
        # ARGUMENT mood
        mood_string = get_mood(mood)

        # Print the name string concatenated with
        # mood_string
        print(name + mood_string)

    print()
    print("  1. Plant a new gremlin seed")
    print("  2. Get the gremlin's advice")
    print("  3. Talk to the gremlin. (Type anything)")
    print("  4. Leave")
    choice = input()
    print()

    #### ---- RESPOND TO INPUT ---- ####
    # --- Quit --- #
    if choice == "4":
        done = True

    # --- New gremlin --- #

    # Else if choice is "1"
    elif choice == "1":

        # Set name to a CALL of the random_name function
        name = random_name()

        # Set mood to a random number between -3 and 3
        mood = random.randint(-3, 3)

    # --- Display advice --- #

    # Else if choice is "2" and name is not ""
    elif choice == "2" and name != "":

        # Print name + the string " says: " + a CALL
        # to the get_advice function with ARGUMENT
        # mood
        print(name + " says: " + get_advice(mood))

    # --- Incorrect input with gremlin --- #
    elif name != "":
        print(name + " seems like maybe it's listening?")
        mood = random.randint(-3, 3)

    # --- Incorrect input with no gremlin --- #
    else:
        print("You need to plant a gremlin seed before you can do anything else.")

# Turn in your Coding Exercise.