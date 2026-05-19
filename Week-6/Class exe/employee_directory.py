# Description: Employee Directory System
# Author: Dimitri Nji

print()

class Employee:
    # Class attribute - shared by all employees
    company = "DataPulse Analytics"

    def __init__(self, name, department, salary):
        # Instance attributes - unique for each employee
        self.name = name
        self.department = department
        self.salary = salary

    def display_info(self):
        print(f"Company: {Employee.company}")
        print(f"Name: {self.name}")
        print(f"Department: {self.department}")
        print(f"Salary: ${self.salary:,.2f}")
        print("-----------------------------")

    def annual_bonus(self):
        bonus = self.salary * 0.10
        print(f"Annual bonus for {self.name}: ${bonus:,.2f}")
        print("-----------------------------")


# Collect input for employee 1
print("=== Enter Employee 1 ===")
name1 = input("Employee name: ")
department1 = input("Department: ")
salary1 = float(input("Monthly salary: "))

print()

# Collect input for employee 2
print("=== Enter Employee 2 ===")
name2 = input("Employee name: ")
department2 = input("Department: ")
salary2 = float(input("Monthly salary: "))

print()

# Create employee objects
employee1 = Employee(name1, department1, salary1)
employee2 = Employee(name2, department2, salary2)

# Call methods for each employee
employee1.display_info()
employee1.annual_bonus()

employee2.display_info()
employee2.annual_bonus()

'''company is the class attribute because every employee belongs
to the same company.self.name, self.department, 
and self.salary are instance attributes because each 
employee has their own name, department, and salary.
display_info() shows the employee’s details.
annual_bonus() takes the employee’s salary and calculates 10% of it.
float(input(...)) is used because salary needs to be a number, 
not a string.'''