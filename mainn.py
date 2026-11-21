
def calculate_grade(average):
    if average >= 90:
        return "S"
    elif average >= 80:
        return "A"
    elif average >= 65:
        return "B"
    elif average >= 50:
        return "C"
    elif average >= 40:
        return "D"
    else:
        return "F"


def main():
    print("===== STUDENT GRADE MANAGEMENT SYSTEM =====")

    name = input("Enter student name: ")
    department = input("Enter department: ")
    semester = input("Enter semester: ")

    print("\nEnter marks out of 100")

    mark1 = float(input("Enter Subject 1 marks: "))
    mark2 = float(input("Enter Subject 2 marks: "))
    mark3 = float(input("Enter Subject 3 marks: "))

    marks = [mark1, mark2, mark3]

    if any(mark < 0 or mark > 100 for mark in marks):
        print("Invalid marks! Enter marks between 0 and 100.")
        return

    average = sum(marks) / 3
    grade = calculate_grade(average)

    print("\n========== STUDENT RESULT ==========")
    print("Student Name:", name)
    print("Department:", department)
    print("Semester:", semester)
    print("Subject 1:", mark1)
    print("Subject 2:", mark2)
    print("Subject 3:", mark3)
    print("Average Marks:", round(average, 2))
    print("Grade:", grade)


if __name__ == "__main__":
    main()
