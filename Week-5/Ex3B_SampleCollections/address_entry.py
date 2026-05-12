
# Create a dictionary with contact information
contact_info = {
    "name": "Dimitri Nji",
    "address": "123 Main Street",
    "city": "Wilmington",
    "state": "DE",
    "zip": "19801"
}

# Print the formatted address using one print statement
print(f"""
{contact_info["name"]}
{contact_info["address"]}
{contact_info["city"]}, {contact_info["state"]} {contact_info["zip"]}
""")

# Remove the name key:value pair
contact_info.pop("name")

# Create a new dictionary for full name
full_name = {
    "first name": "Dimitri",
    "last name": "Nji"
}

# Add honorific using .update()
full_name.update({"honorific": "Mr."})

# Add full_name dictionary to contact_info
contact_info.update({"full_name": full_name})

# Print the updated formatted address
print(f"""
{contact_info["full_name"]["honorific"]} {contact_info["full_name"]["first name"]} {contact_info["full_name"]["last name"]}
{contact_info["address"]}
{contact_info["city"]}, {contact_info["state"]} {contact_info["zip"]}
""")