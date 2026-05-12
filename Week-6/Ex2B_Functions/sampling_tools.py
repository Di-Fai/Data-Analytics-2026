# Description: This script uses random tools to sample and shuffle product data.
# Author: Dimitri Nji

# Import the random module
import random


# Starting list of products
products = [
    'Laptop',
    'Monitor',
    'Keyboard',
    'Mouse',
    'Webcam',
    'Headset',
    'Docking Station',
    'USB Hub',
    'Desk Lamp',
    'Surge Protector'
]


# A) Select one random product as Product of the Day
product_of_the_day = random.choice(products)
print("Product of the Day:", product_of_the_day)


# B) Select 3 products for a usability survey without repeating any product
survey_products = random.sample(products, 3)
print("Products selected for usability survey:", survey_products)


# C) Shuffle all products for a presentation
random.shuffle(products)
print("Products in randomized presentation order:", products)


# D) Generate a simulated daily transaction count between 50 and 300
daily_transaction_count = random.randint(50, 300)
print("Simulated daily transaction count:", daily_transaction_count)



'''
import random lets Python use built-in random tools.
random.choice(products) chooses one random item from the list.
random.sample(products, 3) chooses three different products without repeating any item.
random.shuffle(products) changes the order of the original list. It does not create a new list, 
so you print products after shuffling.
random.randint(50, 300) creates one random whole number between 50 and 300.'''