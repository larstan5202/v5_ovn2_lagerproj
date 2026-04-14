class StockItem:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

class Stock:
    def __init__(self):
        self.items = []

    def add_product(self, product):
        self.items.append(product)

    def decrease_product(self, name, amount):
        for item in self.items:
            if item.name == name:
                if item.amount < amount:
                    return False
                item.amount -= amount
                return True
        return False

