

total = 0
count = 0

print("Enter positive numbers.")
print("Enter a negative number to stop.")
print('----------------------------------------')

while True:
    number = float(input("Enter a number: "))

    if number < 0:
        break

    total += number
    count += 1

print('----------------------------------------')
print("Numbers entered:", count)
print("Sum of numbers entered:", total)
print('----------------------------------------')