# Description: This program creates a RewardsProgram class and adds customers to a customer list
# Author: Dimitri Nji

# Global customer list
# This is created outside the class so it does not reset each time a new customer is created.
cust_list = []


class RewardsProgram:
    """This class stores customer rewards information for a restaurant."""

    def __init__(self, cust_name, phone, email):
        self.cust_name = cust_name
        self.phone = phone
        self.email = email

    def profile(self):
        print(f"Name: {self.cust_name}")
        print(f"Phone: {self.phone}")
        print(f"Email: {self.email}")

    def thank_you(self):
        print(f"Thank you, {self.cust_name}, for visiting our restaurant!")

    def add_to_cust_list(self):
        cust_list.append((self.cust_name, self.phone, self.email))


# Create three customer instances
customer1 = RewardsProgram("Alice Chen", "302-555-1234", "alice@example.com")
customer2 = RewardsProgram("Marcus Brown", "302-555-5678", "marcus@example.com")
customer3 = RewardsProgram("Dimitri Nji", "302-555-9012", "dimitri@example.com")


# Run methods for customer 1
customer1.profile()
customer1.thank_you()
customer1.add_to_cust_list()

print()

# Run methods for customer 2
customer2.profile()
customer2.thank_you()
customer2.add_to_cust_list()

print()

# Run methods for customer 3
customer3.profile()
customer3.thank_you()
customer3.add_to_cust_list()

print()

# Print the full customer list
print("Customer List:")
print(cust_list)

'''This program creates a rewards customer profile, 
prints the customer’s information, thanks the customer, 
and then adds their information to one main customer list without
 overwriting the previous customers.'''