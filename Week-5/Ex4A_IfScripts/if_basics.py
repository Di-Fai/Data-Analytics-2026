# Description: This script practices basic if statements
# Author: Dimitri Nji

x = 100
y = 20

# a) Check if x divided by y is 5
if x / y == 5:
    print("x divided by y is 5")
    x = 1
else:
    print("are the variables set up correctly?")

# b) Check if x times y is equal to y
if x * y == y:
    print("now x times y is y")
    x = 10
else:
    print(f"Whoops, x equals {x}")

# c) Check if x is less than y
if x < y:
    print("x is less than y")
    x = x * 2
else:
    print("uh oh, x is not less than y")

# d) Check if x is greater than y
if x > y:
    print("how is x greater than y??")
else:
    print("x is NOT greater than y")

# e) Print final values
print(f"The final value of x is {x} and the final value of y is {y}")

'''x starts as 100
100 / 20 = 5, so x becomes 1
1 * 20 = 20, which equals y, so x becomes 10
10 is less than 20, so x doubles to 20
20 is not greater than 20
Final x is 20
'''