# Calculate van rentals for a tour group

import math

people = int(input("Enter the number of people going on the tour: "))

van_capacity = 15
van_cost = 250

vans_needed = math.ceil(people / van_capacity)
total_cost = vans_needed * van_cost
cost_per_person = total_cost / people

print(f"Number of people: {people}")
print(f"Vans needed: {vans_needed}")
print(f"Total van rental cost: ${total_cost:.2f}")
print(f"Cost per person: ${cost_per_person:.2f}")

# a) How much money did your script say you had to charge per person?
# 19.74

# b) If you multiply that out, how much did you collect?
# 38 × $19.74 = $750.12

# c) How much were the vans?
# 3 vans × $250 = $750.00

# d) Why do you have leftover money?
# You have leftover money because the cost per person was rounded to two decimal places. 
# Since money cannot be charged in partial cents, 
# rounding each person’s cost to $19.74 causes the group to collect $0.12 more than the exact van cost.