# Description: This script converts department codes using match/case
# Author: Dimitri Nji

dept_code = int(input("Enter department code: "))

match dept_code:
    case 1:
        department = "Marketing"
    case 5:
        department = "Human Resources"
    case 10:
        department = "Accounting"
    case 12:
        department = "Legal"
    case 18:
        department = "IT"
    case 20:
        department = "Customer Relations"
    case _:
        department = "Unknown Department"

print(f"Department Code: {dept_code}")
print(f"Department Name: {department}")


''' The if/elif/else version is easy to understand 
because it checks each condition one at a time. The match/case version
is cleaner when checking one variable against many exact values.
I think match/case is more efficient to read for this problem, 
but if/elif/else is easier for beginners to understand.  '''