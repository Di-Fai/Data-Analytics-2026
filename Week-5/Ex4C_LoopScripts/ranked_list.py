
#  This program uses enumerate to print a ranked list

favorite_foods = ["jollof rice", "tacos", "ramen", "jerk chicken", "pizza"]

for number, food in enumerate(favorite_foods, start=1):
    if number == 1:
        print(str(number) + ". " + food + " <- top pick!")
    else:
        print(str(number) + ". " + food)

print()
print("Bonus reverse list:")

for number, food in enumerate(reversed(favorite_foods), start=1):
    print(str(number) + ". " + food)