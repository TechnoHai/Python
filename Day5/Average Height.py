#🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# print(student_heights)
#🚨 Don't change the code above 👆


#Write your code below this row 👇
# student_heights = [100, 200, 300, 500]
student_number = 0
#count the number that the loop is running .
for student in student_heights:
    student_number += 1

#calculate the sum of height of all the student
student_height_summary = 0
for student in student_heights:
    student_height_summary += student

student_heights_average = round(student_height_summary/student_number)
print(student_heights_average)
