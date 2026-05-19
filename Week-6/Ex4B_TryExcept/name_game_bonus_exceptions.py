# Description: Name game with input validation and exception handling
# Author: Dimitri Nji

# This script asks the user for their name.
# Then it checks for invalid inputs like numbers, single letters, or blank entries.
# The goal is to practice using try, except, else, and finally.


try:
    first_name = input("Enter your first name: ").strip()

    # input() always returns a string.
    # This means typing 123 does NOT automatically cause an error.
    # Python sees it as "123", not the integer 123.
    # So we have to write our own logic to check if the input is invalid.

    if first_name == "":
        raise ValueError("No text was entered.")

    elif first_name.isdigit():
        raise ValueError("Name cannot be only numbers.")

    elif len(first_name) == 1:
        raise ValueError("Name must be more than one letter.")

    elif not first_name.isalpha():
        raise ValueError("Name should only contain letters.")

except ValueError as error:
    print("ValueError:", error)

else:
    print(f"Hello, {first_name}!")
    print(f"Your name has {len(first_name)} letters.")
    print(f"Your name in uppercase is {first_name.upper()}.")

finally:
    print("Let's try another one...")


# ---------------------------------------------------------
# Testing notes:
# ---------------------------------------------------------

# Test input: 123
# Expected: I thought this might throw an error.
# Actual: It does not automatically throw an error because input() stores it as a string.
# Exception handled: ValueError
# Location: The error is raised by this line:
# raise ValueError("Name cannot be only numbers.")

# Test input: A
# Expected: This input works in Python because "A" is still a valid string.
# Actual: It does not throw an automatic error.
# Exception handled: ValueError
# Location: The error is raised by this line:
# raise ValueError("Name must be more than one letter.")

# Test input: just pressing Enter
# Expected: This should be invalid because no name was entered.
# Actual: input() returns an empty string, so Python does not automatically crash.
# Exception handled: ValueError
# Location: The error is raised by this line:
# raise ValueError("No text was entered.")

# Test input: John3
# Expected: This should be invalid because a name should not contain numbers.
# Actual: Python accepts it as a string, so we check it with .isalpha().
# Exception handled: ValueError
# Location: The error is raised by this line:
# raise ValueError("Name should only contain letters.")


# ---------------------------------------------------------
# Challenge answer:
# ---------------------------------------------------------

# In exception handling, raise SystemExit(0) means the program is being stopped on purpose.
# The 0 means the program ended successfully, not because of an error.
# It might be used instead of break when you want to completely exit the whole program,
# not just leave a loop.
# It can produce unexpected results if you use it inside a larger program,
# because it may stop the entire script instead of only stopping one section.
# For small beginner programs, break is usually safer when you only want to exit a loop.