student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}

for name, score in student_scores.items():
    if (score > 90):
        grade = "Outstanding"
    elif (score > 80):
        grade = "Exceeds Expectations"
    elif (score > 70):
        grade = "Acceptable"
    else:
        grade = "Fail"

    student_grades[name] = grade

print(student_grades)


