class RewardsProgram:
    """A class for tracking customer rewards points and restaurants visited."""

    def __init__(self, cust_name, phone, email):
        self.cust_name = cust_name
        self.phone = phone
        self.email = email
        self.restaurants_visited = []
        self.rewards_points = {}

    def profile(self):
        print(f"Name: {self.cust_name}")
        print(f"Phone: {self.phone}")
        print(f"Email: {self.email}")

    def thank_you(self):
        print(f"Thank you, {self.cust_name}, for visiting our restaurant!")

    def calculate_rewards(self, bill_amount):
        points = int(bill_amount)
        return points

    def visit_rest(self):
        restaurant = input("Name of restaurant: ")

        if restaurant not in self.restaurants_visited:
            self.restaurants_visited.append(restaurant)

        bill = float(input("What was the total food bill for this visit? "))

        points = self.calculate_rewards(bill)

        if restaurant in self.rewards_points:
            self.rewards_points[restaurant] += points
        else:
            self.rewards_points[restaurant] = points

        total_points = sum(self.rewards_points.values())

        print(f"Points for this visit: {points}")
        print(f"Total rewards points earned: {total_points}")
        print(f"Thank you for visiting {restaurant}!")

    def print_rewards(self):
        print(f"\nRewards summary for {self.cust_name}:")
        print(f"Restaurants visited: {self.restaurants_visited}")
        print(f"Points by restaurant: {self.rewards_points}")
        print(f"Total points: {sum(self.rewards_points.values())}")


customer1 = RewardsProgram("Dimitri Nji", "302-555-1234", "dimitri@email.com")

customer1.profile()
customer1.visit_rest()
customer1.visit_rest()
customer1.print_rewards()


'''This program tracks a customer’s rewards points. 
When the customer visits a restaurant,
the program asks for the restaurant name and the food bill. 
The bill is converted into points, where every dollar equals one point. 
The program also keeps track of which restaurants the customer has 
visited and how many points they earned at each restaurant.'''