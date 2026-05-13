# Description: This program creates a Restaurant class and uses three restaurant objects
# Author: Dimitri Nji

class Restaurant:
    """This class represents a restaurant with a name and type of food."""

    def __init__(self, rest_name, food_type):
        self.rest_name = rest_name
        self.food_type = food_type

    def describe_rest(self):
        print(f"{self.rest_name} serves {self.food_type}.")

    def rest_open(self):
        print(f"{self.rest_name} is open.")


# Create three instances of the Restaurant class
restaurant1 = Restaurant("Mama's Kitchen", "African food")
restaurant2 = Restaurant("Pizza Palace", "Italian food")
restaurant3 = Restaurant("Tokyo Grill", "Japanese food")


# Call the methods for each restaurant
restaurant1.describe_rest()
restaurant1.rest_open()

restaurant2.describe_rest()
restaurant2.rest_open()

restaurant3.describe_rest()
restaurant3.rest_open()

''' This program creates a Restaurant class that stores a restaurant’s
 name and food type. Then I create three different restaurant objects 
and use methods to describe each restaurant and show that it is open.
'''