"""
Product Invenctory Project:
Create an application which manages an inventory of products.
Create a product class which has a price, id, and quantity on hand.
Then create an inventory class which keeps track of various products and can sum up the inventory value.
"""

class product:
    def __init__(self, price, id, quantity):
        self.price = price
        self.id = id
        self.quantity = quantity

    def change_price(self, new_price):
        if isinstance(new_price, float) == False:
            print("Please enter a decimal number!")
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
            self.quantity = new_quantity
        
    def take_amount(self, taken_amount):
        if isinstance(taken_amount, int) == False:
            print("Please enter a number!")
        else:
            self.quantity -= taken_amount
    
    def add_amount(self, added_amount):
        if isinstance(added_amount, int) == False:
            print("Please enter a number!")
        else:
            self.quantity += added_amount
    
    def get_price(self):
        return self.price
    
    def __str__(self):
        return f"Product: {self.id}\nPrice: {self.price}\nQuantity: {self.quantity}"

class Inventory:
    def __init__(self, products = None):
        self.products = products if products is not None else []

    def add_product(self, new_product):
        if isinstance(new_product, product) == True:
            self.products.append(new_product)
    
    def remove_product(self, product_to_remove):
        if product_to_remove in self.products:
            self.products.remove(product_to_remove)

    def sum_value(self):
        p = 0
        for i in self.products:
            p += i.get_price()
        return p
    
    def __str__(self):
        return "\n".join(str(i) for i in self.products)
    
p1 = product(10.99, "bread", 9)
p2 = product(9.99, "pie", 5)
i1 = Inventory()
i1.add_product(p1)
i1.add_product(p2)
value = i1.sum_value()
print(value)