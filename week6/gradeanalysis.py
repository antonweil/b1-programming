student_records=[]
stats = {}
for i in range(6):
    name = input(f"{i+1}: enter student name: ")
    grade = int(input(f"{i+1}: enter student grade: "))

    student=(name, grade)
    student_records.append(student)

grades = [grade for (name, grade) in student_records]

highest = max(grades)
lowest = min(grades)
average = sum(grades) / len(grades)

stats["highest_grade"] = highest
stats["lowest_grade"] = lowest
stats["average_grade"] = average

unique = []

for grade in grades:
    if grade not in unique:
        unique.append(grade)

collect = {}

for grade in grades:
    collect[grade] = collect.get(grade, 0) +1

print(collect)
print("unique grades: "'[%s]' % ', '.join(map(str, collect)))
print(stats)