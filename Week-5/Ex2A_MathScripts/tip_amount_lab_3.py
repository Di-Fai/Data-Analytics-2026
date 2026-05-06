# Calculates the tip amount on a restaurant bill using user input

# Ask the user for the restaurant bill amount
restaurant_bill = input("What was the restaurant bill amount? ")

# Ask the user for the tip percentage
tip_percentage = input("What tip percentage do you want to leave? ")

# Convert inputs from strings to numbers
restaurant_bill = float(restaurant_bill)
tip_percentage = float(tip_percentage)

# Convert percentage into decimal form
tip_rate = tip_percentage / 100

# Calculate tip amount
tip_amount = restaurant_bill * tip_rate

# Display result
print(
    "The tip on a $" + format(restaurant_bill, ".2f") +
    " restaurant bill is $" + format(tip_amount, ".2f")
)

# Observations:
# The input() function always stores user input as a string.
# Because of that, I had to use float() before doing my math.
# A possible pitfall is that the program will crash if the user types words instead of numbers.
# Another pitfall is that the user must enter only the number for the percentage, such as 20, not 20%.
# If the user enters 20%, Python cannot convert it using float().