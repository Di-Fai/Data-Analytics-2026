price = float(input("Enter the original price: "))
discount = float(input("Enter the discount percentage: "))

final_price = price - (price * discount / 100)

print(f"Final Price = ${final_price:.2f}")