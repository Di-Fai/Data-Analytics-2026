# Define known values
food_cost = 79.25
tax = 6.54
tip = 12.00


# Calculate the unknown
total_due = food_cost + tax + tip

# The str() function converts a value into a string.
# It is used here because total_due is a number, and Python needs it converted to text
# before it can be joined with the sentence inside the print statement.


# Display the results
# print("The total due is " + str(total_due))

print("Food cost is " + str(food_cost) + " and tax is " + str(tax))
# print("Tip is " + str(tip))
print("Total due is " + str(total_due))

print("Tip is " + format(tip, ".2f"))