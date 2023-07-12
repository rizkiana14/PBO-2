class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Inventory:
    def __init__(self):
        self.items = []
    def add_item(self, item, quantity):
        for i in range(quantity):
            self.items.append(item)
    def total_price(self):
        total_price = 0
        for item in self.items:
            total_price += item.price
        return total_price

item1 = Item("Mouse", 250)
item2 = Item("Keyboard", 400)
item3 = Item("Monitor", 1000)

inventory = Inventory()

inventory.add_item(item1, 2)
inventory.add_item(item2, 1)
inventory.add_item(item3, 3)

print(f"Total price of inventory is {inventory.total_price()}")
