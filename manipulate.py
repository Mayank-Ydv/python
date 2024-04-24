def add_student(data, name, grades):
    """Add a new student to the data."""
    data[name] = grades

def remove_student(data, name):
    """Remove a student from the data."""
    if name in data:
        del data[name]
    else:
        print(f"{name} not found in the data.")

def get_student_grades(data, name):
    """Retrieve grades for a student."""
    if name in data:
        return data[name]
    else:
        print(f"{name} not found in the data.")
        return None

def display_students(data):
    """Display all students and their grades."""
    print("Students and Grades:")
    for name, grades in data.items():
        print(f"{name}: {grades}")

# Initialize data
students_data = {
    'Alice': [85, 90, 92],
    'Bob': [78, 85, 80],
    'Charlie': [90, 92, 88]
}

# Display initial data
display_students(students_data)

# Add a new student
add_student(students_data, 'David', [82, 88, 90])
print("\nAfter adding David:")
display_students(students_data)

# Remove a student
remove_student(students_data, 'Bob')
print("\nAfter removing Bob:")
display_students(students_data)

# Get grades for a student
grades = get_student_grades(students_data, 'Alice')
print("\nGrades for Alice:", grades)
