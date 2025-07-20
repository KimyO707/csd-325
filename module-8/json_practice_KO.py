#Kimberly Orozco, Module 8.2 Assignment, July 20th, 2025
#Purpose: Practice with json


import json

def print_student_list(student_list):
    for student in student_list:
        print(f"{student['L_Name']}, {student['F_Name']} : ID = {student['Student_ID']}, Email = {student['Email']}")


with open("student.json", "r") as file:
    students = json.load(file)

print("OG Student List:")
print_student_list(students)  


new_student = {
    "F_Name": "Kimberly",
    "L_Name": "Orozco",
    "Student_ID": 7070,
    "Email": "kmorozco@my365.bellevue.edu"
}
students.append(new_student)

print("\nUpdated Student List:")
print_student_list(students) 

with open("student.json", "w") as file:
    json.dump(students, file, indent=4)

print("\nThe student.json file has been updated.")