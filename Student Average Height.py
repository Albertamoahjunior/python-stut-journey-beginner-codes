student_heights = input("Enter the heights of the students: ").split()
i = 0
sum_of_students = 0
average_student_height = 0

for students in student_heights:
    i += 1

for n in range(0, i):
    student_heights[n] = int(student_heights[n])

for height in student_heights:
    sum_of_students += height

average_student_height = round(sum_of_students/i)

print(average_student_height)