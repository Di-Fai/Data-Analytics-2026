# Description: This script displays a student's major name and department office
# Author: Dimitri Nji

student_name = input("Enter the student's name: ")
student_major = input("Enter the student's major code: ").upper()

major_name = "<unknown>"
department_office = ""

if student_major == "BIOL":
    major_name = "Biology"
    department_office = "Science Bldg, Room 310"

elif student_major == "CSCI":
    major_name = "Computer Science"
    department_office = "Sheppard Hall, Room 314"

elif student_major == "ENG":
    major_name = "English"
    department_office = "Kerr Hall, Room 201"

elif student_major == "HIST":
    major_name = "History"
    department_office = "Kerr Hall, Room 114"

elif student_major == "MKT":
    major_name = "Marketing"
    department_office = "Westly Hall, Room 310"

else:
    major_name = "<unknown>"
    department_office = "<unknown>"

print('-----------------------------------')
print("Student Name:", student_name)
print("Major Code:", student_major)
print("Major Name:", major_name)
print("Department Office:", department_office)


'''
In this program, I used the input function so that i will not have to 
keep changing the values for students Name and Major code manually.
I made it so the user can enter the student’s name and major code. 
The program then takes the major code and changes it to uppercase using .upper(), 
so even if someone types the code in lowercase, the program can still read it correctly.

After that, the program checks the major code using if, elif, and else statements.
If the major code matches one of the codes from the table, 
it displays the correct major name and department office. 
If the code is not in the table, the program shows <unknown>.

At the end, the program prints the student’s name,
major code, major name, and department office in a clear way.
This makes it easy to see the student’s information
based on the major code entered.'''


