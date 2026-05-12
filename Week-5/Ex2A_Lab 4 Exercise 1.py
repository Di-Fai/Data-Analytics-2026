# Program to calculate discounted price

price = float(input("Enter the original price: "))
discount = float(input("Enter the discount percentage: "))

final_price = price - (price * discount / 100)

print(f"The original price is ${price:.2f}")
print(f"The discount percentage is {discount:.2f}%")
print(f"The final price is ${final_price:.2f}")