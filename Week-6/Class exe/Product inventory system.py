

class Product:
    def __init__(self, name, category, price, quantity):
        self.name = name
        self.category = category
        self.price = price
        self.quantity = quantity

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Category: {self.category}")
        print(f"Price: ${self.price:.2f}")
        print(f"Quantity: {self.quantity}")

    def inventory_value(self):
        total = self.price * self.quantity
        print(f"Inventory Value: ${total:.2f}")


print("Enter Product 1")
name1 = input("Product name: ")
category1 = input("Category: ")
price1 = float(input("Price: $"))
quantity1 = int(input("Quantity: "))

print("\nEnter Product 2")
name2 = input("Product name: ")
category2 = input("Category: ")
price2 = float(input("Price: $"))
quantity2 = int(input("Quantity: "))

product1 = Product(name1, category1, price1, quantity1)
product2 = Product(name2, category2, price2, quantity2)

print(f"\nProduct 1: {product1.name} - {product1.category}")
product1.display_info()
product1.inventory_value()

print(f"\nProduct 2: {product2.name} - {product2.category}")
product2.display_info()
product2.inventory_value()

'''This program creates a product class.
 The class stores the product name, category, price, and quantity.
 Then the program asks the user to enter information for two products.
After that, it prints each product’s details and calculates the total 
inventory value by multiplying price times quantity'''

total_inventory = (product1.price * product1.quantity) + (product2.price * product2.quantity)
print(f"\nTotal Inventory Value for Both Products: ${total_inventory:.2f}")

'''I went ahead and added a total inventory value for both
 products at the end of the program. 
 It calculates the total inventory value by summing the 
 inventory values of both products.'''