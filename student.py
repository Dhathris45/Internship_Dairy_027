students = [
    {"name": "John", "age": 20, "course": "Computer Science"},
    {"name": "Emily", "age": 21, "course": "Data Science"}
]


new_student = {"name": "Michael", "age": 22, "course": "Artificial Intelligence"}
students.append(new_student)


students[0]["course"] = "Software Engineering"


print("Student Records:")

for student in students:
    print("Name:", student["name"])
    print("Age:", student["age"])
    print("Course:", student["course"])
    print("-------------------")