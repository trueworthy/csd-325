# trueworthy_JSONPractice

import json

with open("student.json") as f:
    class_list = json.load(f)

import json

def list_of_students(class_list):
    for student in class_list:
        print(f"{student['F_Name']} , {student['L_Name']} : ID = {student['Student_ID']} , Email = {student['Email']}")

    with open("student.json", "r") as read_file:
        class_list = json.load(read_file)

print("This is the original student list:")
print(list_of_students(class_list))

new_student = {"F_Name": "Lea",
               "L_Name": "Trueworthy",
               "Student_ID": "80228",
               "Email": "ltrueworthy@my365.bellevue.edu"
               }

with open("student.json", "w") as f:
    json.dump(new_student, f)

class_list.append(new_student)

# Print updated student list
print("\nThis is the updated student list:")
list_of_students(class_list)

# Update the JSON file with new data
with open('student.json', 'w') as f:
    json.dump(class_list, f, indent=4)

# Notify user that the file has been updated
print("\nThe student data in the JSON file has been updated.")