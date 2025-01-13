"""


import numpy as np


arr = np.array([1, 2, 3, 4, 5])
print("1 D array", arr)


print(type(arr))



a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)



#Puzzle: Find the sum of elements along the dignoal and flip the matrix

#Generate a random 4x4 matrix with values from 1 to 20
matrix = np.random.randint(1, 21, (4, 4))
print("Original Matrix")
print(matrix)

#Calculate the sum of the diagonal
diagonal_sum = np.trace(matrix)
print(f"\nSum of diagonal elements: {diagonal_sum}")

#Flip the matrix vertically and horizontally

flipped_matrix = np.flip(matrix)
print("\nFlipped Matrix: ")
print(flipped_matrix)

#Bonus: Identify positions of elements greater than 15
positions = np.argwhere(matrix > 15)
print("\nPosition of elements greater than 15: ")
for pos in positions:
    print(f"Row{pos[0] + 1}, Column{pos[1] + 1}")


import csv

# File path for the sales tracker
file_path = "sales_tracker.csv"

# Create a new CSV file with headers
def create_csv():
    headers = ["Date", "Product", "Quantity", "Price per unit", "Total"]
    with open(file_path, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(headers)
    print("Data has been created.")

# Add a new sale record to the CSV file
def add_sale(date, product, quantity, price_per_unit):
    total = quantity * price_per_unit
    with open(file_path, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, product, quantity, price_per_unit, total])
    print("Sale record added.")

# Calculate total sales from the CSV file
def calculate_total_sales():
    total_sales = 0
    with open(file_path, mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            total_sales += float(row["Total"])
    print(f"Total Sales: ${total_sales:.2f}")

# Example usage
create_csv()
add_sale("2025-01-08", "Laptop", 2, 1200.50)
add_sale("2025-01-09", "Mouse", 5, 25.99)
calculate_total_sales()



Task: Analyze Sales Data
You are given a CSV file named sales_data.csv that contains the following columns:
Product: The name of the product.
Region: The region where the sales occurred.
Sales: The number of units sold.
Price: The price of the product.
Your task is to:
Read the CSV file into Python using the csv module.
Calculate Total Sales Revenue for each product by multiplying the sales by the price.
Use NumPy to:
Calculate the average revenue for all products.
Find the product with the highest revenue.
Find the total revenue by region.
Write the results (product name, total revenue, and region) to a new CSV file called sales_summary.csv.
"""
"""
import csv

file_path = "sales_data.csv"
summary_path = "sales_summary.csv"
import numpy as np

def create_csv():
    headers = ["Product", "Region", "Sale", "Price", "Total"]
    with open(file_path, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(headers)
    print("Sales tracker created.")

def add_sale(product, region, sale, price):
    total = sale * price
    with open(file_path, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([product, region, sale, price, total])
    print("Sale record added.")

def calculate_total_sales():
    total_sales = 0
    revenues = []
    products = []
    regions = {}
    
    with open(file_path, mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            total_sales += float(row["Total"])
            revenues.append(float(row["Total"]))
            products.append(row["Product"])
            # Summing revenues by region
            if row["Region"] in regions:
                regions[row["Region"]] += float(row["Total"])
            else:
                regions[row["Region"]] = float(row["Total"])
    
    avg_revenue = np.mean(revenues)
    highest_revenue_product = products[np.argmax(revenues)]
    
    print(f"Total Sales: ${total_sales:.2f}")
    print(f"Average Revenue: ${avg_revenue:.2f}")
    print(f"Highest Revenue Product: {highest_revenue_product}")
    
    # Write the summary to a new CSV file
    with open(summary_path, mode="w", newline="") as summary_file:
        writer = csv.writer(summary_file)
        writer.writerow(["Product", "Total Revenue", "Region"])
        
        for region, revenue in regions.items():
            writer.writerow([highest_revenue_product, revenue, region])

create_csv()
add_sale("Apple", "Hilly", 5, 25.50)
add_sale("Banana", "Hilly", 9, 29.99)
calculate_total_sales()




#next process

import csv
import random
import numpy as np

sales_data_path = "sales_data.csv"
summary_data_path = "sales_summary.csv"

def create_csv():
    headers = ["Product", "Region", "Sale", "Price", "Total"]
    with open(sales_data_path, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(headers)
    print("Sales tracker created.")

def add_sale(product, region, sale, price):
    total = sale * price
    with open(sales_data_path, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([product, region, sale, price, total])
    print("Sale record added.")

def generate_random_sales_data(num_records):
    products = ["Laptop", "Smartphone", "Tablet", "Headphones", "Mouse"]
    regions = ["Pokhara", "Kathmandu", "Birgunj", "Illam"]

    for _ in range(num_records):
        product = random.choice(products)
        region = random.choice(regions)
        sales = random.randint(10, 500)  # Random units sold
        price = round(random.uniform(10.0, 2000.0), 2)  # Random price
        add_sale(product, region, sales, price)

    print(f"Generated {num_records} random sales records.")

def analyze_sales_data():
    sales_data = []
    # Read data from the sales CSV
    with open(sales_data_path, mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            row["Sale"] = int(row["Sale"])
            row["Price"] = float(row["Price"])
            row["Total"] = float(row["Total"])
            sales_data.append(row)

    # Calculate metrics using NumPy
    revenue = np.array([row["Total"] for row in sales_data])
    average_revenue = np.mean(revenue)
    product_revenue_map = {}
    region_revenue_map = {}

    for row in sales_data:
        product = row["Product"]
        region = row["Region"]
        product_revenue_map[product] = product_revenue_map.get(product, 0) + row["Total"]
        region_revenue_map[region] = region_revenue_map.get(region, 0) + row["Total"]

    product_with_highest_revenue = max(product_revenue_map, key=product_revenue_map.get)

    # Write the summary to a new CSV
    with open(summary_data_path, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Product", "Total Revenue", "Region"])
        for row in sales_data:
            writer.writerow([row["Product"], row["Total"], row["Region"]])

    # Output results
    print("\nAnalysis Summary:")
    print(f"Average Revenue: ${average_revenue:.2f}")
    print(f"Product with Highest Revenue: {product_with_highest_revenue} (${product_revenue_map[product_with_highest_revenue]:.2f})")
    print("Total Revenue by Region:")
    for region, revenue in region_revenue_map.items():
        print(f" - {region}: ${revenue:.2f}")

        
# Create the CSV file and add random sales data
create_csv()
generate_random_sales_data(1000)

# Analyze the sales data
analyze_sales_data()

"""