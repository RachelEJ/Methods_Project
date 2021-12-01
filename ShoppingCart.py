class ShoppingCart:
    def __init__(self, userId, db):
        self.userId = userId
        self.items = []
        self.db = db
    def addItem(self, sku, quantity):
        self.items.append((sku, quantity))
        self.db.addCartItem(self.userId, sku, quantity)

    def removeItem(self, sku):
        i = 0
        while (i < len(self.items)):
            if (self.items[i][0] == sku):
                self.items.pop(i)
                self.db.removeCartItem(self.user, sku)
            i += 1

        

    def changeQuantity(self, sku, newQuantity):
        i = 0
        while (i < len(self.items)):
            if (self.items[i][0] == sku):
                self.items[i] = (sku, newQuantity)
            i += 1
    
    def getItems(self):
        return self.items