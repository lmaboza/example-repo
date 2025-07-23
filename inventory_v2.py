import os


#========The beginning of the class==========
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
    shoe_list.clear()
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "inventory.txt")
    try:
        with open(file_path, "r") as file:
            next(file)  # skip header
            for line in file:
                parts = line.strip().split(",")
                if len(parts) == 5:
                    country, code, product, cost, quantity = parts
                    shoe = Shoe(country, code, product, cost, quantity)
                    shoe_list.append(shoe)
    except FileNotFoundError:
        print("Error: inventory.txt file not found in the current directory.")
    except PermissionError:
        print("Error: No permission to read the file.")
    except UnicodeDecodeError:
        print("Error: File contains invalid characters.")
    except Exception as e:
        print(f"Unexpected error: {str(e)}")

def update_inventory_file():
    '''
    Overwrite inventory.txt with the current content of shoe_list.
    '''
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "inventory.txt")
    try:
        with open(file_path, "w") as file:
            file.write("Country,Code,Product,Cost,Quantity\n")
            for shoe in shoe_list:
                file.write(f"{shoe.country},{shoe.code},{shoe.product},{shoe.cost},{shoe.quantity}\n")
    except PermissionError:
        print("Error: No permission to write to the file.")
    except Exception as e:
        print(f"Could not write to file: {e}")

def capture_shoes():
    '''
    Capture user input to create a new Shoe object and add to shoe_list.
    '''
    try:
        country = input("Enter country: ").strip()
        code = input("Enter product code: ").strip()
        product = input("Enter product name: ").strip()
        
        while True:
            cost = input("Enter product cost: ")
            try:
                cost = float(cost)
                if cost >= 0:
                    break
                print("Cost cannot be negative. Please try again.")
            except ValueError:
                print("Please enter a valid number.")
        
        while True:
            quantity = input("Enter product quantity: ")
            try:
                quantity = int(quantity)
                if quantity >= 0:
                    break
                print("Quantity cannot be negative. Please try again.")
            except ValueError:
                print("Please enter a whole number.")
                
        shoe = Shoe(country, code, product, cost, quantity)
        shoe_list.append(shoe)
        update_inventory_file()
        print("Shoe added successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

def view_all():
    '''
    Print all Shoe objects in shoe_list.
    '''
    if not shoe_list:
        print("No shoes available.")
        return
    
    print("\n=== ALL SHOES IN INVENTORY ===")
    print(f"{'Country':<15} {'Code':<10} {'Product':<20} {'Price':<10} {'Qty':<5}")
    print("-" * 65)
    for shoe in shoe_list:
        print(f"{shoe.country:<15} {shoe.code:<10} {shoe.product:<20} R{shoe.cost:<8.2f} {shoe.quantity:<5}")

def re_stock():
    '''
    Find the Shoe with the lowest quantity and offer to restock it.
    '''
    if not shoe_list:
        print("No shoes available.")
        return
    
    lowest = min(shoe_list, key=lambda s: s.get_quantity())
    print(f"\nLowest stock item: {lowest}")
    
    while True:
        try:
            restock_qty = input("Enter quantity to restock (or 'cancel' to abort): ")
            if restock_qty.lower() == 'cancel':
                print("Restock cancelled.")
                return
                
            restock_qty = int(restock_qty)
            if restock_qty <= 0:
                print("Quantity must be positive.")
                continue
                
            lowest.quantity += restock_qty
            update_inventory_file()
            print(f"Stock updated. New quantity: {lowest.quantity}")
            break
        except ValueError:
            print("Invalid quantity entered. Please enter a number or 'cancel'.")

def search_shoe():
    '''
    Search for a Shoe by code and print it.
    '''
    if not shoe_list:
        print("No shoes available to search.")
        return
        
    code = input("Enter shoe code to search: ").strip().lower()
    found_shoes = [shoe for shoe in shoe_list if shoe.code.lower() == code]
    
    if found_shoes:
        print("\n=== SEARCH RESULTS ===")
        for shoe in found_shoes:
            print(shoe)
    else:
        print(f"No shoe found with code: {code}")

def value_per_item():
    '''
    Print the total value of each shoe (cost * quantity).
    '''
    if not shoe_list:
        print("No shoes available.")
        return
    
    print("\n=== INVENTORY VALUE ===")
    print(f"{'Product':<20} {'Code':<10} {'Value':<15}")
    print("-" * 45)
    for shoe in shoe_list:
        value = shoe.get_cost() * shoe.get_quantity()
        print(f"{shoe.product:<20} {shoe.code:<10} R{value:<14.2f}")

def highest_qty():
    '''
    Find the Shoe with the highest quantity and display it as being for sale.
    '''
    if not shoe_list:
        print("No shoes available.")
        return
    
    highest = max(shoe_list, key=lambda s: s.get_quantity())
    print("\n=== HIGHEST QUANTITY ITEM (MARK FOR SALE) ===")
    print(highest)
    print("This item should be marked for promotion!")

def edit_shoe():
    '''
    Edit an existing shoe in the inventory.
    '''
    if not shoe_list:
        print("No shoes available to edit.")
        return
        
    code = input("Enter shoe code to edit: ").strip().lower()
    for shoe in shoe_list:
        if shoe.code.lower() == code:
            print(f"\nCurrent details: {shoe}")
            try:
                # Get new values or keep current if empty input
                new_country = input(f"Enter new country [{shoe.country}]: ").strip()
                shoe.country = new_country if new_country else shoe.country
                
                new_product = input(f"Enter new product name [{shoe.product}]: ").strip()
                shoe.product = new_product if new_product else shoe.product
                
                while True:
                    new_cost = input(f"Enter new cost [R{shoe.cost:.2f}]: ").strip()
                    if not new_cost:
                        break
                    try:
                        shoe.cost = float(new_cost)
                        if shoe.cost >= 0:
                            break
                        print("Cost cannot be negative.")
                    except ValueError:
                        print("Please enter a valid number.")
                
                while True:
                    new_qty = input(f"Enter new quantity [{shoe.quantity}]: ").strip()
                    if not new_qty:
                        break
                    try:
                        shoe.quantity = int(new_qty)
                        if shoe.quantity >= 0:
                            break
                        print("Quantity cannot be negative.")
                    except ValueError:
                        print("Please enter a whole number.")
                
                update_inventory_file()
                print("\nShoe updated successfully.")
                print(f"New details: {shoe}")
            except Exception as e:
                print(f"An error occurred: {e}")
            return
    
    print(f"No shoe found with code: {code}")

def delete_shoe():
    '''
    Delete a shoe from the inventory.
    '''
    if not shoe_list:
        print("No shoes available to delete.")
        return
        
    code = input("Enter shoe code to delete: ").strip().lower()
    for i, shoe in enumerate(shoe_list):
        if shoe.code.lower() == code:
            print(f"\nShoe to delete: {shoe}")
            confirm = input("Are you sure you want to delete this shoe? (y/n): ").lower()
            if confirm == 'y':
                del shoe_list[i]
                update_inventory_file()
                print("Shoe deleted successfully.")
            else:
                print("Deletion cancelled.")
            return
    
    print(f"No shoe found with code: {code}")

def low_stock_report(threshold=5):
    '''
    Generate a report of shoes with quantity below specified threshold.
    '''
    if not shoe_list:
        print("No shoes available.")
        return
    
    low_stock = [shoe for shoe in shoe_list if shoe.quantity < threshold]
    
    if not low_stock:
        print(f"No items with quantity below {threshold}.")
        return
    
    print(f"\n=== LOW STOCK REPORT (Below {threshold} items) ===")
    print(f"{'Product':<20} {'Code':<10} {'Qty':<5} {'Price':<10}")
    print("-" * 45)
    for shoe in sorted(low_stock, key=lambda s: s.quantity):
        print(f"{shoe.product:<20} {shoe.code:<10} {shoe.quantity:<5} R{shoe.cost:<8.2f}")

#==========Main Menu=============
def main_menu():
    while True:
        print("\n=== Nike Warehouse Inventory System ===")
        print("1. Read shoe data")
        print("2. Add new shoe")
        print("3. View all shoes")
        print("4. Restock lowest quantity shoe")
        print("5. Search shoe by code")
        print("6. Calculate value per item")
        print("7. Show shoe with highest quantity")
        print("8. Edit shoe details")
        print("9. Delete shoe")
        print("10. Low stock report")
        print("11. Exit")

        choice = input("\nSelect an option (1-11): ").strip()

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
            edit_shoe()
        elif choice == "9":
            delete_shoe()
        elif choice == "10":
            threshold = input("Enter low stock threshold (default 5): ").strip()
            try:
                threshold = int(threshold) if threshold else 5
                low_stock_report(threshold)
            except ValueError:
                print("Invalid threshold. Using default value 5.")
                low_stock_report()
        elif choice == "11":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid option. Please enter a number between 1-11.")

if __name__ == "__main__":
    main_menu()