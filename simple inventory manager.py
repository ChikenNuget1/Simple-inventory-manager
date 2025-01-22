"""
Product Invenctory Project:
Create an application which manages an inventory of products.
Create a product class which has a price, id, and quantity on hand.
Then create an inventory class which keeps track of various products and can sum up the inventory value.
"""
from datetime import datetime
import os


class Product:
    def __init__(self, price, id, quantity):
        self.price = price
        self.id = id.lower()
        self.quantity = int(quantity)

    def change_price(self, new_price):
        if isinstance(new_price, float) == False:
            print("Please enter a decimal number!")
        else:
            if new_price < 0:
                print("The entered price is a negative number.\nPlease try again!")
            else:
                self.price = new_price
    
    def change_id(self, new_id):
        if isinstance(new_id, str) == False:
            print("Please enter a name!")
        else:
            self.id = new_id

    def change_quantity(self, new_quantity):
        if isinstance(new_quantity, int) == False:
            print("Please enter a number!")
        else:
            if new_quantity < 0:
                print("The entered quantity is a negative number.\nPlease try again!")
            else:
                self.quantity = new_quantity
        
    def take_amount(self, taken_amount):
        if isinstance(taken_amount, int) == False:
            print("Please enter a number!")
        else:
            if self.quantity - taken_amount < 0:
                print("That will result in a negative number!. Please try again")
            else:
                self.quantity -= taken_amount
    
    def add_amount(self, added_amount):
        if isinstance(added_amount, int) == False:
            print("Please enter a number!")
        else:
            self.quantity += added_amount
    
    def get_price(self):
        return self.price

    def get_quantity(self):
        return self.quantity

    def get_id(self):
        return self.id
    
    def __str__(self):
        return f"Product: {self.id}\nPrice: ${self.price}\nQuantity: {self.quantity}\n"


class Inventory:
    def __init__(self, products = None):
        self.products = products if products is not None else []

    def add_product(self, new_product):
        if isinstance(new_product, Product) == True:
            self.products.append(new_product)
    
    def remove_product(self):
        print("="*33)
        print("\n".join(str(i) for i in self.products))
        product_to_remove = input("Which product would you like to remove(Please enter the product ID)? ").lower()
        for i in self.products:
            current_id = i.get_id()
            if current_id == product_to_remove:
                o = i
        if o != 0:
            self.products.remove(o)
        else:
            print("That product ID does not exist!")

    def sum_value(self):
        p = 0
        for i in self.products:
            p += (i.get_price() * i.get_quantity())
        return p
    
    def search_product(self, id):
        for i in self.products:
            current_id = i.get_id()
            if current_id == id:
                return i
        return "That ID does not exist"
    
    def check_stock(self):
        low_stock = []
        stock_threshold = "ab"
        while not isinstance(stock_threshold, int):
            try:
                stock_threshold = int(input("What is the threshold for low stock? "))
            except ValueError:
                print("Please enter a valid integer")
        for i in self.products:
            current_stock = i.get_quantity()
            if current_stock <= stock_threshold:
                low_stock.append(i)
        return low_stock
    
    def create_report(self):
        try:
            f = open("inventory_report.txt", 'x')
        except FileExistsError:
            print("File already exists. Please delete the previous one")
            return None
        low_stock = self.check_stock()
        total_value = self.sum_value()
        current_datetime = datetime.now()
        f.write(f"Inventory report {current_datetime}\n")
        f.write("="*33)
        f.write("\n")
        f.write("\n".join(str(i) for i in self.products))
        f.write("="*33)
        f.write("\n")
        f.write("Products with low stock are: \n")
        f.write("\n".join(str(i) for i in low_stock))
        f.write("="*33)
        f.write("\n")
        f.write(f"Total inventory value is ${total_value}")

    def delete_report(self):
        if os.path.exists("inventory_report.txt"):
            os.remove("inventory_report.txt")
        else:
            print("The file does not exist.")
            print("Please create a new report.")

    def __str__(self):
        return "\n".join(str(i) for i in self.products)

    def __len__(self):
        return len(self.products)


class Manager:
    def __init__(self):
        self.manager_inventory = Inventory()
        self.main_menu()

    def main_menu(self):
        print("="*33)
        print(str(self.manager_inventory))
        print("="*33)
        print("Main Menu")
        print("1 to add product")
        print("2 to change price")
        print("3 to change quantity")
        print("4 to remove a product")
        print("5 to create a report")
        print("6 to delete previous report")
        print("7 to end program")
        user_choice = int(input("Please enter your choice: "))
        match user_choice:
            case 1:
                self.add_product()
            case 2:
                self.price_change()
            case 3:
                self.quantity_change()
            case 4:
                self.product_remove()
            case 5:
                self.report_create()
            case 6:
                self.report_delete()
            case 7:
                quit()

    def add_product(self):
        product_id = 1
        while not isinstance(product_id, str):
            product_id = input("Please enter the product name: ")
        product_price = "ab"
        while not isinstance(product_price, float):
            try:
                product_price = float(input("Please enter the price of the product: "))
            except ValueError:
                print("Please enter a number for the price")
        product_quantity = "ab"
        while not isinstance(product_quantity, float):
            try:
                product_quantity = float(input("Please enter the quantity of the product: "))
            except ValueError:
                print("Please enter a number for the price")
        
        new_product = Product(product_price, product_id, product_quantity)
        self.manager_inventory.add_product(new_product)
        self.main_menu()
        
    def price_change(self):
        if len(self.manager_inventory) == 0:
            print("\nYou must first add a product!\n")
            self.main_menu()
        product_to_change = 10
        while not isinstance(product_to_change, str):
            product_to_change = input("Which product should be changed? ")
        price_into = "ab"
        while not isinstance(price_into, float):
            try:
                price_into = float(input("What price should it be? "))
            except ValueError:
                pass
        product_class = self.manager_inventory.search_product(product_to_change)
        product_class.change_price(price_into)
        self.main_menu()
    
    def quantity_change(self):
        if len(self.manager_inventory) == 0:
            print("\nYou must first add a product!\n")
            self.main_menu()
        product_to_change = 10
        while not isinstance(product_to_change, str):
            product_to_change = input("Which product should be changed? ")
        quantity_into = "ab"
        while not isinstance(quantity_into, int):
            try:
                quantity_into = int(input("What should be the new quantity? "))
            except ValueError:
                pass
        product_class = self.manager_inventory.search_product(product_to_change)
        product_class.change_quantity(quantity_into)

    def product_remove(self):
        if len(self.manager_inventory) == 0:
            print("\nYou must first add a product!\n")
            self.main_menu()
        self.manager_inventory.remove_product()
        self.main_menu()

    def report_create(self):
        self.manager_inventory.create_report()
        self.main_menu()
    
    def report_delete(self):
        self.manager_inventory.delete_report()
        self.main_menu()


if __name__ == "__main__":
    k = Manager()
