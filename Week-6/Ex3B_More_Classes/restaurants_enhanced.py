# Description: Enhanced restaurant class with customers served and ratings
# Author: Dimitri Nji

class Restaurant:
    """A class that stores restaurant information, customers served, and customer ratings."""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
        self.customer_ratings = []

    def describe_restaurant(self):
        print(f"{self.restaurant_name} serves {self.cuisine_type} food.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is open.")

    def add_num_served(self):
        while True:
            try:
                customers = int(input("How many customers served today? "))

                if customers >= 0:
                    self.number_served += customers
                    break
                else:
                    print("Please enter a positive number.")

            except ValueError:
                print("Invalid input. Please enter a whole number.")

    def print_num_served(self):
        print(f"{self.restaurant_name} has served {self.number_served} customers.")

    def customer_rating(self):
        while True:
            try:
                rating = int(input("How would you rate your experience today on a scale of 1-5? "))

                if rating >= 1 and rating <= 5:
                    self.customer_ratings.append(rating)

                    average = sum(self.customer_ratings) / len(self.customer_ratings)

                    print(f"Your rating was {rating}.")
                    print(f"The average rating for this restaurant is {average:.2f}.")
                    break

                else:
                    print("Invalid rating. Please enter a number from 1 to 5.")

            except ValueError:
                print("Invalid input. Please enter a whole number from 1 to 5.")


# Create example restaurants
restaurant1 = Restaurant("Taste of Africa", "African")
restaurant2 = Restaurant("Pasta Palace", "Italian")
restaurant3 = Restaurant("Sushi World", "Japanese")


# Test restaurant 1
print("\n--- Restaurant 1 ---")
restaurant1.describe_restaurant()
restaurant1.open_restaurant()

restaurant1.print_num_served()
restaurant1.add_num_served()
restaurant1.add_num_served()
restaurant1.print_num_served()

restaurant1.customer_rating()
restaurant1.customer_rating()
restaurant1.customer_rating()


# Test restaurant 2
print("\n--- Restaurant 2 ---")
restaurant2.describe_restaurant()
restaurant2.open_restaurant()

restaurant2.print_num_served()
restaurant2.add_num_served()
restaurant2.add_num_served()
restaurant2.print_num_served()

restaurant2.customer_rating()
restaurant2.customer_rating()
restaurant2.customer_rating()


# Test restaurant 3
print("\n--- Restaurant 3 ---")
restaurant3.describe_restaurant()
restaurant3.open_restaurant()

restaurant3.print_num_served()
restaurant3.add_num_served()
restaurant3.add_num_served()
restaurant3.print_num_served()

restaurant3.customer_rating()
restaurant3.customer_rating()
restaurant3.customer_rating()

'''The program does not crash. It asks the user to enter a whole number from 1 to 5.
So this meets the requirement to handle incorrect values.'''