# Dimitri Nji
# 5/12/2026
# multiple parameters
# Python automatically packages multiple return values into a tuple


def greeting(name, city, hobby):
    return name, city, hobby

name = input("Please enter your name: ")
city = input("Please enter your city: ")
hobby = input("Please enter your hobby: ")
result = greeting(name, city, hobby)

print(f"Hello, {result[0]}! I see you are from {result[1]} and enjoy {result[2]}.")
