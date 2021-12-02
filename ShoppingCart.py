class ShoppingCart:
    def __init__(self, userId, db):
        self.userId = userId
        self.items = []
        self.db = db

    def addItem(self, sku, quantity):
        #checks if item actually exists
        actualItem = self.db.getItemBySku(sku)
        if (actualItem == False or actualItem.quantity < quantity):
            return False
        
        while (i < len(self.items)):
            if (self.items[i][0] == sku):
                return False
            i += 1

        self.items.append((sku, quantity))
        self.db.addCartItem(self.userId, sku, quantity)
        return True

    def removeItem(self, sku):
        i = 0
        remCheck = 0
        while (i < len(self.items)):
            if (self.items[i][0] == sku):
                self.items.pop(i)
                self.db.removeCartItem(self.userId, sku)
                remCheck += 1
            i += 1
        if (remCheck > 0):
            return True
        else:
            return False

    def changeQuantity(self, sku, newQuantity):
        i = 0
        while (i < len(self.items)):
            if (self.items[i][0] == sku):
                self.items[i] = (sku, newQuantity)
            i += 1
    
    def getItems(self):
        return self.items

