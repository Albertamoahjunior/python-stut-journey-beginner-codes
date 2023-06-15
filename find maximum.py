student_scores = input("Enter the scores of the students: ").split()

i =0
temp = 0
x = 0

for student in student_scores:
    i += 1

for n in range(0, i):
    student_scores[n] = int(student_scores[n])

for score in student_scores:

    if temp < score:
        temp = score

print(temp)