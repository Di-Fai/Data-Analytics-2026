# Description: This script practices creating and calling custom functions.
# Author: Dimitri Nji


# Function 1: Display a mailing label
def display_mailing_label(name, address, city, state, zip):
    print(name)
    print(address)
    print(f"{city}, {state} {zip}")


# Function 2: Add any amount of numbers
def add_numbers(*numbers):
    total = sum(numbers)

    number_text = " + ".join(str(num) for num in numbers)

    print(f"{number_text} = {total}")


# Function 3: Display a receipt
def display_receipt(total_due, amount_paid):
    print(f"Total Due: ${total_due:.2f}")
    print(f"Amount Paid: ${amount_paid:.2f}")

    if amount_paid >= total_due:
        change_due = amount_paid - total_due
        print(f"Change Due: ${change_due:.2f}")
    else:
        remaining_balance = total_due - amount_paid
        print(f"Remaining Balance: ${remaining_balance:.2f}")


# Test display_mailing_label() twice
print("Mailing Label 1:")
display_mailing_label("Dimitri Nji", "123 Main Street", "Wilmington", "DE", "19801")

print("\nMailing Label 2:")
display_mailing_label("Rebecca Yang", "456 Market Street", "Newark", "DE", "19711")


# Test add_numbers() three times
print("\nAdding Numbers:")
add_numbers(10)
add_numbers(10, 20)
add_numbers(5, 10, 15, 20)


# Test display_receipt() three times
print("\nReceipt 1: Overpaid")
display_receipt(25.00, 30.00)

print("\nReceipt 2: Paid Exact")
display_receipt(40.00, 40.00)

print("\nReceipt 3: Underpaid")
display_receipt(50.00, 35.00)