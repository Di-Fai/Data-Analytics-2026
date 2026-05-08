# Description: This script calculates gross pay including overtime

pay_rate = float(input("Enter your pay rate: "))
hours_worked = float(input("Enter your hours worked: "))

# If hours are more than 40, calculate overtime pay
if hours_worked > 40:
    regular_hours = 40
    overtime_hours = hours_worked - 40

    regular_pay = regular_hours * pay_rate
    overtime_pay = overtime_hours * pay_rate * 1.5

    gross_pay = regular_pay + overtime_pay
else:
    gross_pay = hours_worked * pay_rate

print(f"Pay Rate: ${pay_rate:.2f}")
print(f"Hours Worked: {hours_worked}")
print(f"Gross Pay: ${gross_pay:.2f}")