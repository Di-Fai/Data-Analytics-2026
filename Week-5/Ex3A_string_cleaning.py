# Description: This script cleans messy string data
# Author: Dimitri Nji

# Original contact records
name_1 = "PRIYA SHARMA"
name_2 = "bob NGUYEN"
name_3 = "LaTonya Williams"

salary_1 = "$82,500"
salary_2 = "$74,000"

print("--- Lowercase Names ---")

name_1_lower = name_1.lower()
name_2_lower = name_2.lower()
name_3_lower = name_3.lower()

print(name_1_lower)
print(name_2_lower)
print(name_3_lower)

print("\n--- Title Case Names ---")

name_1_title = name_1.title()
name_2_title = name_2.title()
name_3_title = name_3.title()

print(name_1_title)
print(name_2_title)
print(name_3_title)

print("\n--- Remove Dollar Signs ---")

salary_1_no_dollar = salary_1.replace("$", "")
salary_2_no_dollar = salary_2.replace("$", "")

print(salary_1_no_dollar)
print(salary_2_no_dollar)

print(type(salary_1_no_dollar))
print(type(salary_2_no_dollar))

# These are still strings.
# To do math with them, we need to remove the comma and convert them to integers.

print("\n--- Convert Salary to Integer ---")

salary_1_int = int(salary_1.replace("$", "").replace(",", ""))

print(salary_1_int)
print(type(salary_1_int))