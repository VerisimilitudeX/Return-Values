"""
SimpleRecursiveInput

Description: Recursive functions to get valid inputs
"""

def get_string(string):
    return input(string)

def get_int(string):
    l_nums = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    x = get_string(string)
    check = True
    for i in x:
        if not i in l_nums:
            check = False
    if check:
        return int(x)
    print("Improper input\n")
    return get_int(string)

def get_char(string):
    x = get_string(string)
    if len(x) == 1:
        return chr(x)
    print("Improper input\n")
    return get_int(string)

def get_array_str():
    length = get_int("Input array len: ")
    array = []
   
    for i in range(length):
        array.append(get_string("Input array item at index " + str(i) + ": "))
   
    return array

def get_array_int():
    length = get_int("Input array len: ")
    array = []
   
    for i in range(length):
        array.append(get_int("Input array item at index " + str(i) + ": "))
   
    return array

def get_array_chr():
    length = get_int("Input array len: ")
    array = []
   
    for i in range(length):
        array.append(get_char("Input array item at index " + str(i) + ": "))
   
    return array
