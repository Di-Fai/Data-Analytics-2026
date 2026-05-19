# Description: Practice raising and handling common Python exceptions
# Author: Dimitri Nji


# -------------------------------
# 1. ValueError Example 1
# -------------------------------

try:
    number = int("hello")  # This raises ValueError because "hello" cannot become an integer

except ValueError:
    print("ValueError: Oops, you tried to convert a value into the wrong data type.")

else:
    print(number)

finally:
    print("Let's try another one...")


# -------------------------------
# 1. ValueError Example 2
# -------------------------------

try:
    price = float("twenty dollars")  # This raises ValueError because this is not a valid float

except ValueError:
    print("ValueError: Oops, this value cannot be converted into a decimal number.")

else:
    print(price)

finally:
    print("Let's try another one...")


# -------------------------------
# 2. NameError Example 1
# -------------------------------

try:
    m = banana  # This raises NameError because banana was never defined

except NameError:
    print("NameError: Oops, looks like you tried to use a variable that does not exist.")

else:
    print(m)

finally:
    print("Let's try another one...")


# -------------------------------
# 2. NameError Example 2
# -------------------------------

try:
    print(student_name)  # This raises NameError because student_name was never created

except NameError:
    print("NameError: Oops, you tried to print a variable before assigning a value to it.")

else:
    print(student_name)

finally:
    print("Let's try another one...")


# -------------------------------
# 3. TypeError Example 1
# -------------------------------

try:
    result = "5" + 10  # This raises TypeError because Python cannot add a string and an integer

except TypeError:
    print("TypeError: Oops, you tried to combine two values with incompatible data types.")

else:
    print(result)

finally:
    print("Let's try another one...")


# -------------------------------
# 3. TypeError Example 2
# -------------------------------

try:
    length = len(100)  # This raises TypeError because an integer has no length

except TypeError:
    print("TypeError: Oops, you used a function on the wrong type of object.")

else:
    print(length)

finally:
    print("Let's try another one...")


# -------------------------------
# 4. SyntaxError Example 1
# -------------------------------

try:
    exec("if True print('Hello')")  # This raises SyntaxError because the if statement is missing a colon

except SyntaxError:
    print("SyntaxError: Oops, your code is written in a way Python cannot understand.")

else:
    print("The code ran successfully.")

finally:
    print("Let's try another one...")


# -------------------------------
# 4. SyntaxError Example 2
# -------------------------------

try:
    exec("for i in range(3)\n    print(i)")  # This raises SyntaxError because the for loop is missing a colon

except SyntaxError:
    print("SyntaxError: Oops, your loop is missing proper Python syntax.")

else:
    print("The code ran successfully.")

finally:
    print("Let's try another one...")

#2a. 
'''Challenge answer: Some inputs that I expected to throw an error actually worked. For example,
typing 123 does not automatically cause an error because the input() function stores everything as a string. 
So 123 becomes "123". A single letter also works because it is still a valid string. 
Pressing Enter also works because Python treats it as an empty string.
To check for these issues, I can use logic like .isdigit(), .isalpha(), len(), and .strip(). 
If the input does not meet the requirements, I can manually raise a ValueError.'''

#2b. 
'''The main exception type I used was ValueError. 
It occurs when the user enters invalid input, such as no text, only numbers, one letter, or characters that are not letters. 
The exception is raised inside the if/elif validation checks after the user enters their input.'''