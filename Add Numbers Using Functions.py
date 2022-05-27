"""
LESSON: 6.2 - Return Values
WARMUP 1
"""

#### --------------------------- ####
#### ---- SUM LIST FUNCTION ---- ####
#### --------------------------- ####
def sum_list(num_list):
    total = 0
    for num in nums:
        total += num

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
    print("Current Total: ")

    # Call sum_list function here
    sum_list(nums)

print()
print("FINAL TOTAL: ")
# Call sum_list function here
sum_list(nums)

