1#========The beginning of the class==========
class Shoe:

    def __init__(self, country, code, product, cost, quantity):
        '''
        Initialise the shoe attributes.
        '''
        self.country = country
        self.code = code
        self.product = product
        self.cost = float(cost)
        self.quantity = int(quantity)

    def get_cost(self):
        '''
        Return the cost of the shoe.
        '''
        return self.cost

    def get_quantity(self):
        '''
        Return the quantity of the shoe.
        '''
        return self.quantity

    def __str__(self):
        '''
        Return a string representation of the shoe.
        '''
        return f"{self.country} | {self.code} | {self.product} | R{self.cost:.2f} | Qty: {self.quantity}"


#=============Shoe list===========
'''
The list will be used to store a list of objects of shoes.
'''
shoe_list = []


#==========Functions outside the class==============
def read_shoes_data():
    '''
    Read inventory.txt and populate the shoe_list with Shoe objects.
    '''
    try:
        with open("inventory.txt", "r") as file:
            next(file)  # skip header
            for line in file:
                parts = line.strip().split(",")
                if len(parts) == 5:
                    country, code, product, cost, quantity = parts
                    shoe = Shoe(country, code, product, cost, quantity)
                    shoe_list.append(shoe)
    except FileNotFoundError:
        print("Error: inventory.txt file not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def capture_shoes():
    '''
    Capture user input to create a new Shoe object and add to shoe_list.
    '''
    try:
        country = input("Enter country: ")
        code = input("Enter product code: ")
        product = input("Enter product name: ")
        cost = float(input("Enter product cost: "))
        quantity = int(input("Enter product quantity: "))
        shoe = Shoe(country, code, product, cost, quantity)
        shoe_list.append(shoe)
        print("Shoe added successfully.")
    except ValueError:
        print("Please enter valid numeric values for cost and quantity.")

def view_all():
    '''
    Print all Shoe objects in shoe_list.
    '''
    if not shoe_list:
        print("No shoes available.")
        return
    for shoe in shoe_list:
        print(shoe)

def re_stock():
    '''
    Find the Shoe with the lowest quantity and offer to restock it.
    '''
    if not shoe_list:
        print("No shoes available.")
        return
    lowest = min(shoe_list, key=lambda s: s.get_quantity())
    print(f"Lowest stock item: {lowest}")
    try:
        restock_qty = int(input("Enter quantity to restock: "))
        lowest.quantity += restock_qty
        print("Stock updated.")
    except ValueError:
        print("Invalid quantity entered.")

def search_shoe():
    '''
    Search for a Shoe by code and print it.
    '''
    code = input("Enter shoe code to search: ").strip()
    for shoe in shoe_list:
        if shoe.code == code:
            print(f"Shoe found: {shoe}")
            return
    print("Shoe not found.")

def value_per_item():
    '''
    Print the total value of each shoe (cost * quantity).
    '''
    for shoe in shoe_list:
        value = shoe.get_cost() * shoe.get_quantity()
        print(f"{shoe.product} ({shoe.code}) - Total Value: R{value:.2f}")

def highest_qty():
    '''
    Find the Shoe with the highest quantity and display it as being for sale.
    '''
    if not shoe_list:
        print("No shoes available.")
        return
    highest = max(shoe_list, key=lambda s: s.get_quantity())
    print(f"Shoe for sale: {highest}")


#==========Main Menu=============
while True:
    print("\nNike Warehouse Inventory Menu")
    print("1. Read shoe data")
    print("2. Capture new shoe")
    print("3. View all shoes")
    print("4. Restock lowest quantity shoe")
    print("5. Search shoe by code")
    print("6. Calculate value per item")
    print("7. Show shoe with highest quantity")
    print("8. Exit")

    choice = input("Select an option (1-8): ")

    if choice == "1":
        read_shoes_data()
    elif choice == "2":
        capture_shoes()
    elif choice == "3":
        view_all()
    elif choice == "4":
        re_stock()
    elif choice == "5":
        search_shoe()
    elif choice == "6":
        value_per_item()
    elif choice == "7":
        highest_qty()
    elif choice == "8":
        print("Exiting the program.")
        break
    else:
        print("Invalid option. Please try again.")
