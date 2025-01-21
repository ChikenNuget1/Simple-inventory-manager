"""
Product Invenctory Project:
Create an application which manages an inventory of products.
Create a product class which has a price, id, and quantity on hand.
Then create an inventory class which keeps track of various products and can sum up the inventory value.
"""

"""
Goal for tomorrow. 
Implement the manager class
    - Will be able to create product objects through the manager class
    - Will be able to access the inventory class
    - Will also be able to change the price and quantity of objects

Add commenting
    - Comment your code so that it becomes readable before making the code public to github for any feedback :)
"""
from datetime import datetime
import os

class product:
    def __init__(self, price, id, quantity):
        self.price = price
        self.id = id.lower()
        self.quantity = quantity

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
        if isinstance(new_product, product) == True:
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


class Manager:
    def __init__(self):
        self.manager_inventory = Inventory()
    
#    def add_product(self):
    
#    def change_price(self):
    
#    def change_quantity(self):
    


p1 = product(10.99, "bread", 5)
p2 = product(9.99, "pie", 5)
i = Inventory()
i.add_product(p1)
i.add_product(p2)
i.delete_report()
