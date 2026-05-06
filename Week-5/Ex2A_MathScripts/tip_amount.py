# Tip Amount = Restaurant Bill × Tip Percentage
# Example : $80 bill × 20% tip = $16 tip
# Since 20% could be written in decimal as 0.20, i will be using the decimal form in my calculations 


# Calculates the tip amount on a restaurant bill

# Define restaurant bill and tip percentage
restaurant_bill = 80.71
tip_percentage = 0.20

# Calculate tip amount
tip_amount = restaurant_bill * tip_percentage

# Display result
print("The tip on a $" + format(restaurant_bill, ".2f") 
      + " restaurant bill is $" + format(tip_amount, ".2f"))