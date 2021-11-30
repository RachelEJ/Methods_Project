class PurchaseHistory:
    def __init__(self, historyID, shoppingCart):
        self.historyID = historyID
        self.items = shoppingCart.getItems()
    
    def addCartToHistory(self, shoppingCart):
        self.items = shoppingCart.getItems()

    def getItems(self):
        return self.items