class PurchaseHistory:
    def __init__(self, historyID):
        self.historyID = historyID
        self.items = []

    def addItem(self, sku, quantity):
        self.items.append((sku, quantity))
    
    def addCartToHistory(self, shoppingCart):
        self.items = shoppingCart.getItems()

    def getItems(self):
        return self.items