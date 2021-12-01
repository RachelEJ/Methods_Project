class Item:
    def __init__(self, name, sku, price, quantity, description):
        self.name = name
        self.sku = sku
        self.price = price
        self.quantity = quantity
        

    def getName(self):
        return self.name

    def getSKU(self):
        return self.sku
    def getPrice(self):
        return self.price

    def getQuantity(self):
        return self.quantity

    

    def changeQuantity(self, quantity):
        self.quantity = quantity

        
