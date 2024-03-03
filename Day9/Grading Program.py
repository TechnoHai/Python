student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
# 🚨 Don't change the code above 👆

# TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

# TODO-2: Write your code below to add the grades to student_grades.👇
for student_name in student_scores:
    if student_scores[student_name] >= 91:  # check if which student have a score higher then 91
        student_grades[student_name] = "Outstanding"  # give the student that have a score higher than 91 "outstanding
    elif 81 <= student_scores[student_name] <= 90:
        student_grades[student_name] = "Exceeds Expectation"
    elif 71 <= student_scores[student_name] <= 80:
        student_grades[student_name] = "Acceptable"
    else:
        student_grades[student_name] = "Fail"

    # 🚨 Don't change the code below 👇
print(student_grades)

