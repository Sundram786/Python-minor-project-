def calculate_grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    else:
        return "F"

students = []

def add_student():
    name = input("Enter student name: ")
    roll_no = input("Enter roll number: ")
    marks = float(input("Enter marks (0-100): "))
    grade = calculate_grade(marks)

    student = {
        "name": name,
        "roll_no": roll_no,
        "marks": marks,
        "grade": grade
    }

    students.append(student)
    print("Student added successfully!\n")

def display_students():
    if not students:
        print("No student records found.\n")
        return

    print("\nStudent Records")
    print("-" * 50)
    for student in students:
        print(f"Name     : {student['name']}")
        print(f"Roll No  : {student['roll_no']}")
        print(f"Marks    : {student['marks']}")
        print(f"Grade    : {student['grade']}")
        print("-" * 50)

def search_student():
    name = input("Enter student name to search: ")
    found = False

    for student in students:
        if student["name"].lower() == name.lower():
            print("\nStudent Found")
            print(f"Name    : {student['name']}")
            print(f"Roll No : {student['roll_no']}")
            print(f"Marks   : {student['marks']}")
            print(f"Grade   : {student['grade']}\n")
            found = True
            break

    if not found:
        print("Student not found.\n")

def main():
    while True:
        print("====== Student Grade Management System ======")
        print("1. Add Student")
        print("2. Display All Students")
        print("3. Search Student")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_student()
        elif choice == '2':
            display_students()
        elif choice == '3':
            search_student()
        elif choice == '4':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.\n")

if __name__ == "__main__":
    main()
