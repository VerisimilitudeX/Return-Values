"""
LESSON: 6.2 - Return Values
TECHNIQUE 2: Multiple Return Values
DEMO
"""

#### --------------------------------- ####
#### ---- GET TOP SCORES FUNCTION ---- ####
#### --------------------------------- ####
def get_top_scores(names, grades):
    top_scores = []
    student = ""

    for i in range(len(names)):
        if grades[i] >= 90:
            top_scores.append(names[i])
    return student


#### ---------------------- ####
#### ---- MAIN PROGRAM ---- ####
#### ---------------------- ####
# Setup
names = []
grades = []

#### ---- INPUT LOOP ---- ####
curr_name = ""
while curr_name != "done":

    # Get student
    curr_name = input("Enter a student name (or done): ")
    if curr_name == "done":
        break

    # Get grade
    curr_grade = int(input("Enter a grade 0 - 100: "))
    print()

    # Add to lists
    names.append(curr_name)
    grades.append(curr_grade)


#### ---- FINAL OUTPUT ---- ####
# Intro
print()
print("The students with grades above 90 are: ")

# Print the students
top_students = get_top_scores(names, grades)
print(top_students)