# Description: This script displays a greeting based on the current hour
# Author: Dimitri Nji

current_hour = int(input("Enter the current hour from 0 to 23: "))

if current_hour >= 23 or current_hour < 4:
    print("What are you doing up so late??")
elif current_hour < 10:
    print("Good morning!")
elif current_hour < 17:
    print("Good day!")
else:
    print("Good evening!")