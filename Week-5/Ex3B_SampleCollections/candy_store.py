# Description: This script practices tuples, sets, indexing, and output
# Author: Dimitri Nji

# Create two tuples
candy_types = ("Gummies", "Lollipops", "Hard Candy")
fruit_flavors = ("Mango", "Strawberry", "Watermelon")

# Create a set to store candy combinations
candy_combinations = {
    candy_types[0] + " - " + fruit_flavors[1],
    candy_types[1] + " - " + fruit_flavors[2],
    candy_types[2] + " - " + fruit_flavors[0]
}

# Print the candy options
print("Today's candy options include:")
print(candy_combinations)

# Print multiple times to observe the order
print("Today's candy options include:")
print(candy_combinations)

print("Today's candy options include:")
print(candy_combinations)

# Observation:
# Sets do not keep a guaranteed order.
# The items may not print in the same order that I typed them.