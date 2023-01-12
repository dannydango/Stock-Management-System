# Imports
import csv
from tabulate import tabulate

# Create the Shoes class
class Shoe:
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = int(cost)
        self.quantity = int(quantity)

    def get_cost(self):
        return self.cost

    def get_quantity(self):
        return self.quantity

    def __str__(self):
        return f"{self.country}, {self.code}, {self.product}, {self.cost}, {self.quantity}"

# Create an empty list to store the shoe objects
shoes_list = []

# Define the read_shoes_data function
def read_shoes_data():
    try:
        with open("inventory.txt", "r") as file:
            reader = csv.reader(file)
            # Skip the first line
            next(reader)
            for row in reader:
                # Create a Shoe object and append it to the shoes_list
                shoes_list.append(Shoe(*row))
    except Exception as e:
        print(f"Error reading from file: {e}")

# Define the capture_shoes function
def capture_shoes():
    country = input("Enter the country of manufacture: ")
    code = input("Enter the code: ")
    product = input("Enter the product name: ")
    cost = input("Enter the cost: ")
    quantity = input("Enter the quantity: ")
    # Create a Shoe object and append it to the shoes_list
    shoes_list.append(Shoe(country, code, product, cost, quantity))
    try:
        # Write the new data to the file
        with open("inventory.txt", "a", newline='') as file:
            writer = csv.writer(file)
            writer.writerow([country, code, product, cost, quantity])
    except Exception as e:
        print(f"Error updating file: {e}")


# Define the view_all function
def view_all():
    # Create a list of lists with the details of the shoes
    shoes_data = [[shoe.country, shoe.code, shoe.product, shoe.quantity] for shoe in shoes_list]
    # Add headings to the table
    headings = ['Country', 'Code', 'Product', 'Quantity']
    # Print the table
    print(tabulate(shoes_data, headers=headings))


# Define the re_stock function
def re_stock():
    # Find the shoe with the lowest quantity
    min_quantity_shoe = min(shoes_list, key=lambda x: x.quantity)
    # Ask the user if they want to add more of this shoe
    answer = input(f"Do you want to add more {min_quantity_shoe.product} shoes? (y/n) ")
    if answer.lower() == "y":
        # Update the quantity of the shoe
        min_quantity_shoe.quantity += int(input("Enter the quantity to add: "))
        # Update the quantity in the file
        update_file(min_quantity_shoe)

# Define the search_shoe function
def search_shoe():
    code = input("Enter the code of the shoe you want to search: ")
    # Search for the shoe in the shoes_list
    found_shoe = next((shoe for shoe in shoes_list if shoe.code == code), None)
    if found_shoe:
        # Print the details of the shoe
        print(found_shoe)
    else:
        print("Shoe not found")

# Define the value
# Define the value_per_item function
def value_per_item():
    # Calculate the total value for each item

    for shoe in shoes_list:
        shoe.cost = int(shoe.cost)
        shoe.quantity = int(shoe.quantity)
        value = shoe.cost * shoe.quantity
        print(f"The total value for {shoe.product} shoes is {value}")

# Define the highest_qty function
def highest_qty():
    # Find the shoe with the highest quantity
    max_quantity_shoe = max(shoes_list, key=lambda x: x.quantity)
    # Print the details of the shoe
    print(f"The {max_quantity_shoe.product} shoes are for sale. Quantity: {max_quantity_shoe.quantity}")

# Define the update_file function
def update_file(shoe):
    try:
        # Read the data from the file
        shoes_data = []
        with open("inventory.txt", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                shoes_data.append(row)
                if row[1] == shoe.code:
                    # Update the quantity for this shoe
                    row[4] = shoe.quantity
        # Write the updated data to the file
        with open("inventory.txt", "w", newline='') as file:
            writer = csv.writer(file)
            writer.writerows(shoes_data)
    except Exception as e:
        print(f"Error updating file: {e}")


# Read the data from the file
read_shoes_data()

# Display the menu
while True:
    print("Menu:")
    print("1. Add new product")
    print("2. View all shoes")
    print("3. Re-stock shoes (Lowest quantity)")
    print("4. Search for a shoe")
    print("5. Calculate value per item")
    print("6. Determine product with highest quantity for sale")
    print("7. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        capture_shoes()
    elif choice == "2":
        view_all()
    elif choice == "3":
        re_stock()
    elif choice == "4":
        search_shoe()
    elif choice == "5":
        value_per_item()
    elif choice == "6":
        highest_qty()
    elif choice == "7":
        break
    else:
        print("That is an invalid input, please try again")