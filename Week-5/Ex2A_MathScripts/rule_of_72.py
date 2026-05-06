# The Rule of 72 estimates how long it takes money to double.
# Years to double = 72 / interest rate
# if the interest rate is 12%: 72 / 12 = 6 years

# Calculates how long it will take savings to double using the Rule of 72

# Define known values
current_savings = 16000.21
interest_rate = 0.12

# Calculate doubled savings and years to double
doubled_savings = current_savings * 2
years_to_double = 72 / (interest_rate * 100)

# Display the results
print("Your current savings is " + format(current_savings, ".2f") + ".")
print(
"At a " + format(interest_rate, ".0%") +
" interest rate, your savings account will be worth " +
format(doubled_savings, ".2f") +
" in " + format(years_to_double, ".0f") + " years"
)