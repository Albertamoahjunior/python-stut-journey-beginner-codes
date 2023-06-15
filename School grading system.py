student_scores ={
"Harry":88,
"Ron":78,
"Hermione":99,
"Draco":74,
"Nerville":62,
}

student_grades = {}
grade = 0
for name in student_scores:
    grade = student_scores[name]
    if grade > 79:
        student_grades[name] = "A"
    elif grade > 69:
        student_grades[name] = "B"
    elif grade > 59:
        student_grades[name] = "C"
    elif grade > 49:
        student_grades[name] = "D"
    elif grade > 39:
        student_grades[name] = "E"
    else:
        student_grades[name] = "F"
print(student_scores)
print(student_grades)