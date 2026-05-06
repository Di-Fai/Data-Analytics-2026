# Assets are things you own that have value, such as:
# Cash, savings, car value, house value, investments.

# Debts are money you owe, such as:
# Credit card debt, car loan, student loan, personal loan

# Formula for Net worth:  Net Worth = Total Assets - Total Debts

# Calculates net worth using assets and debts

# Define assets
cash = 2400.25
savings = 16000.10
car_value = 36000.12

# Define debts
credit_card_debt = 15.23
car_loan = 30000.15
student_loan = 100.2

# Calculate totals
total_assets = cash + savings + car_value
total_debts = credit_card_debt + car_loan + student_loan
net_worth = total_assets - total_debts

# Display results
print("Your total assets are " + format(total_assets, ".2f"))
print("Your total debts are " + format(total_debts, ".2f"))
print("Your net worth is " + format(net_worth, ".2f"))