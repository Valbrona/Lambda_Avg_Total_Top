avg = lambda seq: sum(seq) / len(seq)
total = lambda seq: sum(seq)
top = lambda seq: max(seq)

operations = {
    "average": avg,
    "total": total,
    "top": top
}
students = [
    {"name": "Rolf", "grades": (98, 68, 55, 99, 89)},
    {"name": "Charlie", "grades": (89, 77, 49, 88, 56)},
    {"name": "Anna", "grades": (100, 56, 67, 45, 87)},
    {"name": "Jen", "grades": (99, 82, 73, 49, 64)}
]

for student in students:
    name = student["name"]
    grades = student["grades"]

    print(f"Student: {name}")
    operation = input("Enter 'average', 'total' or 'top': ")

    if operation in operations:
        operation_function = operations[operation]
        print(operation_function(grades))
    else:
        print("Does not exist")