import json
import os

class StudentManagementSystem:
    """
    A system to manage student data using CRUD operations: Create, Read, Update, and Delete.
    Implements nested dictionary to store student data.
    Tracks transactions in a log file.
    """
    def __init__(self):
        self.students = {}
        self.faculty_students = {}
        self.log_file = "transaction_log.txt"
        self._initialize_log()

    def _initialize_log(self):
        """Creates or clears the log file."""
        with open(self.log_file, "w") as file:
            file.write("Transaction Log\n")

    def _log_transaction(self, message):
        """Logs a transaction to the log file."""
        with open(self.log_file, "a") as file:
            file.write(f"{message}\n")

    def add_student(self):
        """
        Adds a new student to the system, including subjects with marks and fees.
        Validates input dynamically.
        """
        try:
            student_id = input("Enter a Serial Number: ").strip()
            if student_id in self.students:
                print("Student with this Serial Number already exists.")
                return

            fname = input("Enter a First Name: ").strip()
            while not fname.isalpha():
                print("Invalid input. First name must contain only letters.")
                fname = input("Enter a valid First Name: ").strip()

            lname = input("Enter a Last Name: ").strip()
            while not lname.isalpha():
                print("Invalid input. Last name must contain only letters.")
                lname = input("Enter a valid Last Name: ").strip()

            contact = input("Enter a Contact Number: ").strip()
            while not (contact.isdigit() and len(contact) == 10):
                print("Invalid input. Contact number must be a 10-digit number.")
                contact = input("Enter a valid Contact Number: ").strip()

            subjects = {}
            while True:
                subject_name = input("Enter a Subject: ").strip()
                marks = input(f"Enter marks for {subject_name}: ").strip()
                while not marks.isdigit():
                    print("Invalid input. Marks must be a number.")
                    marks = input(f"Enter valid marks for {subject_name}: ").strip()
                
                fees = input(f"Enter fees for {subject_name}: ").strip()
                while not fees.isdigit():
                    print("Invalid input. Fees must be a number.")
                    fees = input(f"Enter valid fees for {subject_name}: ").strip()

                subjects[subject_name] = {"marks": int(marks), "fees": int(fees)}

                add_more = input("Do you want to add another subject? (y/n): ").strip().lower()
                if add_more != 'y':
                    break

            self.students[student_id] = {
                "fname": fname,
                "lname": lname,
                "contact": contact,
                "subjects": subjects
            }
            print("Student added successfully.")
            self._log_transaction(f"Added student: {student_id} - {fname} {lname}")

        except Exception as e:
            print(f"An error occurred: {e}")

    def view_students(self):
        """
        Displays all students in the system.
        """
        if not self.students:
            print("No students in the system.")
        else:
            print("\nList of Students:")
            for student_id, details in self.students.items():
                print(f"{student_id}: {details}")

    def view_specific_student(self):
        """
        Displays details of a specific student by ID.
        Validates the ID dynamically.
        """
        student_id = input("Enter Student Serial Number to view: ").strip()
        if student_id in self.students:
            print(self.students[student_id])
        else:
            print("Student not found.")

    def delete_student(self):
        """
        Deletes a student from the system.
        Validates the ID dynamically.
        """
        student_id = input("Enter Student Serial Number to delete: ").strip()
        if student_id in self.students:
            confirmation = input("Are you sure you want to delete this student? (y/n): ").strip().lower()
            if confirmation == 'y':
                del self.students[student_id]
                print("Student deleted successfully.")
                self._log_transaction(f"Deleted student: {student_id}")
            else:
                print("Deletion cancelled.")
        else:
            print("Student not found.")

    def add_marks_faculty(self):
        """
        Faculty-specific functionality to add marks for their own students.
        """
        faculty_name = input("Enter your name (Faculty): ").strip()
        student_id = input("Enter the Student Serial Number: ").strip()

        if student_id not in self.students:
            print("Student not found.")
            return

        subject_name = input("Enter the subject to add/update marks: ").strip()
        if subject_name not in self.students[student_id]["subjects"]:
            print("Subject not found for the student.")
            return

        marks = input(f"Enter marks for {subject_name}: ").strip()
        while not marks.isdigit():
            print("Invalid input. Marks must be a number.")
            marks = input(f"Enter valid marks for {subject_name}: ").strip()

        self.students[student_id]["subjects"][subject_name]["marks"] = int(marks)
        print("Marks updated successfully.")
        self._log_transaction(f"Faculty {faculty_name} updated marks for {student_id}: {subject_name} = {marks}")

    def view_faculty_students(self):
        """
        Faculty-specific functionality to view all their students.
        """
        faculty_name = input("Enter your name (Faculty): ").strip()
        print("\nStudents List:")
        for student_id, details in self.students.items():
            print(f"{student_id}: {details}")


def display_menu(role):
    """
    Displays the menu based on the selected role.
    """
    if role == "1":
        print("\n1. Add Student")
        print("2. Remove Student")
        print("3. View All Students")
        print("4. View Specific Student")
        print("5. Exit")
    elif role == "2":
        print("\n1. Add Marks to Student")
        print("2. View All Students")
        print("3. Exit")


def main():
    """
    Demonstrates the CRUD operations of the Student Management System.
    """
    sms = StudentManagementSystem()

    while True:
        print("\nRole Selection")
        print("Press 1 for Counselor")
        print("Press 2 for Faculty")

        role = input("Enter a role ID: ").strip()

        if role == "1":
            while True:
                display_menu(role)
                choice = input("Enter a choice by Counselor: ").strip()

                if choice == '1':
                    sms.add_student()

                elif choice == '2':
                    sms.delete_student()

                elif choice == '3':
                    sms.view_students()

                elif choice == '4':
                    sms.view_specific_student()

                elif choice == '5':
                    print("Exiting Counselor menu.")
                    break

                else:
                    print("Invalid choice. Please try again.")

        elif role == "2":
            while True:
                display_menu(role)
                choice = input("Enter a choice by Faculty: ").strip()

                if choice == '1':
                    sms.add_marks_faculty()

                elif choice == '2':
                    sms.view_faculty_students()

                elif choice == '3':
                    print("Exiting Faculty menu.")
                    break

                else:
                    print("Invalid choice. Please try again.")

        else:
            print("Invalid role. Please try again.")


if __name__ == "__main__":
    main()