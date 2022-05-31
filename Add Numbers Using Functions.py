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
    sum_list(nums)

print()
print("FINAL TOTAL: ")

sum_list(nums)
