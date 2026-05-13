# Description: This program collects sales information and prints a sales summary report

def sales_summary(name, region, units, price):
    revenue = units * price
    bonus = revenue * 0.10
    return revenue, bonus


# Collect user input
name = input("Associate name: ")
region = input("Store region: ")
units = int(input("Units sold: "))
price = float(input("Price per unit $: "))

# Call the function
revenue, bonus = sales_summary(name, region, units, price)

# Print formatted report
print(f"""
===== RetailEdge Inc. — Sales Summary =====
Associate : {name}
Region    : {region}
Units sold: {units}
Unit price: ${price:.2f}
-------------------------------------------
Total revenue              : ${revenue:.2f}
Performance bonus (10%)    : ${bonus:.2f}
===========================================
""")