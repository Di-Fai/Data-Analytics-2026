# Description: This script converts department codes to department names
# Author: Dimitri Nji

dept_code = int(input("Enter department code: "))

if dept_code == 1:
    department = "Marketing"
elif dept_code == 5:
    department = "Human Resources"
elif dept_code == 10:
    department = "Accounting"
elif dept_code == 12:
    department = "Legal"
elif dept_code == 18:
    department = "IT"
elif dept_code == 20:
    department = "Customer Relations"
else:
    department = "Unknown Department"

print(f"Department Code: {dept_code}")
print(f"Department Name: {department}")