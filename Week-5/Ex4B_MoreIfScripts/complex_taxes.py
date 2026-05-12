# Description: This script calculates gross pay, tax, and net pay
# Author: Dimitri Nji

pay_rate = float(input("Enter your pay rate: "))
hours_worked = float(input("Enter hours worked: "))
filing_status = input("Enter filing status: single or joint: ").lower()

# Calculate weekly gross pay
if hours_worked > 40:
    overtime_hours = hours_worked - 40
    gross_pay = (40 * pay_rate) + (overtime_hours * pay_rate * 1.5)
else:
    gross_pay = hours_worked * pay_rate

# Calculate annual gross income
annual_income = gross_pay * 52

# Choose tax rate based on filing status and annual income
if filing_status == "single":
    if annual_income < 30000:
        tax_rate = 0.10
    elif annual_income < 60000:
        tax_rate = 0.12
    else:
        tax_rate = 0.22

elif filing_status == "joint":
    if annual_income < 60000:
        tax_rate = 0.10
    elif annual_income < 100000:
        tax_rate = 0.12
    else:
        tax_rate = 0.22

else:
    tax_rate = 0
    print("Invalid filing status.")

# Calculate tax and net pay
tax_withheld = gross_pay * tax_rate
net_pay = gross_pay - tax_withheld

print(f"You worked {hours_worked} hours this period.")
print(f"Because you earn ${pay_rate:.2f} per hour, your gross weekly pay is ${gross_pay:.2f}.")
print(f"Your filing status is {filing_status}.")
print(f"Your tax withholding for the week is ${tax_withheld:.2f}.")
print(f"Your net pay is ${net_pay:.2f}.")


'''
1. Asks for pay rate, hours worked, and filing status.
2. Calculates gross weekly pay.
3. Estimates yearly income by multiplying weekly pay by 52.
4. Uses the filing status and yearly income to choose a tax rate.
5. Calculates tax withheld and net pay.
'''