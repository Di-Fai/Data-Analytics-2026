# Description: This script tests various numeric
# conversion techniques
# Author: Dimitri Nji

# Original variables
a = " 101.1 "
b = '55'
c = "402 Stevens"
d = 'Number 5 '

# Print original values and types
print("Original variables:")
print(a, type(a))
print(b, type(b))
print(c, type(c))
print(d, type(d))

print("\n--- Conversion Tests ---")

# Variable a
# a_int = int(a)  # ValueError: cannot convert decimal string directly to int
a_float = float(a)
a_float_then_int = int(float(a))
a_sliced = float(a[1:6])
a_stripped = a.strip()

print("\nVariable a:")
print(a_float, type(a_float))
print(a_float_then_int, type(a_float_then_int))
print(a_sliced, type(a_sliced))
print(a_stripped, type(a_stripped))

# Variable b
b_int = int(b)
b_float = float(b)
b_sliced = int(b[0:2])

print("\nVariable b:")
print(b_int, type(b_int))
print(b_float, type(b_float))
print(b_sliced, type(b_sliced))

# Variable c
# c_int = int(c)  # ValueError: cannot convert letters and numbers together to int
# c_float = float(c)  # ValueError: cannot convert letters and numbers together to float
c_sliced = int(c[0:3])

print("\nVariable c:")
print(c_sliced, type(c_sliced))

# Variable d
# d_int = int(d)  # ValueError: cannot convert text to int
# d_float = float(d)  # ValueError: cannot convert text to float
d_sliced = int(d[7:8])
d_stripped = d.strip()

print("\nVariable d:")
print(d_sliced, type(d_sliced))
print(d_stripped, type(d_stripped))

# Notes:
# int() works only when the string contains a whole number, like "55".
# float() works when the string contains a decimal number, like "101.1".
# int(float(a)) works because "101.1" is first converted to 101.1, then to 101.
# Slicing lets us pull out only the numeric part of a string.
# .strip() removes extra spaces from the beginning and end of a string.