# Description: This program prints sales performance for each salesperson
# Author: Dimitri Nji

sales_data = [
    ("Marcus Webb", "East", 4250.00),
    ("Priya Sharma", "West", 5875.50),
    ("DeShawn Carter", "East", 3100.75),
    ("LaTonya Rivers", "South", 6420.00),
    ("Bob Nguyen", "West", 4980.25),
]

total_sales = 0

for name, region, sales in sales_data:
    print(f"{name} ({region}): ${sales:,.2f}")

    if sales > 5000:
        print("^ Top performer!")

    total_sales = total_sales + sales

print()
print(f"Overall total sales: ${total_sales:,.2f}")

'''This program uses a list of sales records. 
Each record has the salesperson’s name, region, 
and sales amount. The loop goes through each record and prints a summary.
 If someone made more than $5,000, the program marks them as a top performer.
At the end, it prints the total sales for everyone.'''