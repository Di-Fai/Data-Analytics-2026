# calculate the average of three numbers

name = input("Enter your name: ")

first_number = float(input("Enter first number: "))
second_number = float(input("Enter second number: "))
third_number = float(input("Enter third number: "))

average = (first_number + second_number + third_number) / 3

print(f"Hello {name}, The average of {first_number:g}, {second_number:g} and {third_number:g} is: {average:.2f}")