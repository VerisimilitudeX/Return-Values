"""
LESSON: 6.2 - Return Values
WARMUP 1
"""

#### --------------------------- ####
#### ---- SUM LIST FUNCTION ---- ####
#### --------------------------- ####
def sum_list(num_list):
    if len(num_list) == 0:
        return 0
    total = 0
    for num in num_list:
        total += num

    return(total)

#### ---------------------- ####
#### ---- MAIN PROGRAM ---- ####
#### ---------------------- ####
nums = []
val = ""

while val != "done":
    val = input("Enter a number or done: ")

    print()
    if val == "done":
        break

    nums.append(float(val))
    amount = sum_list(nums)

    print("Current Total: " + str(amount))
  


# Call sum_list function here
amount = sum_list(nums)
print()
print("FINAL TOTAL: " + str(amount))