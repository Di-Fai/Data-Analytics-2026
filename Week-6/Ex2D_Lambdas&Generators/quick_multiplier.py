# Description: This script demonstrates lambda functions
# Author: Dimitri Nji

# 1. Create a doubler lambda function
doubler = lambda n: n * 2

# Test doubler
print("Doubler tests:")
print(doubler(8))
print(doubler(-4))
print(doubler("banana"))

print()

# 2. Create a tripler lambda function
tripler = lambda n: n * 3

# Test tripler
print("Tripler tests:")
print(tripler(8))
print(tripler(-4))
print(tripler("banana"))

print()

# 3. Create a multiplier function
def multiplier(number):
    return lambda n: n * number


# 4. Create multiplier variables
quadrupler = multiplier(4)
quintupler = multiplier(5)
sextupler = multiplier(6)
septupler = multiplier(7)
octupler = multiplier(8)
nonupler = multiplier(9)
decupler = multiplier(10)

# 5. Test each multiplier
print("Multiplier tests:")
print("Quadrupler:", quadrupler(2))
print("Quintupler:", quintupler(2))
print("Sextupler:", sextupler(2))
print("Septupler:", septupler(2))
print("Octupler:", octupler(2))
print("Nonupler:", nonupler(2))
print("Decupler:", decupler(2))