class PurchaseHistory:
    def __init__(self, userid, historyID, db, cart = None):
        self.userid = userid
        self.historyID = historyID
        self.db = db
        self.items = []
        if (cart!= None):
            self.addCartToHistory(cart)

    def addItem(self, sku, quantity):
        self.items.append((sku, quantity))
    
    def addCartToHistory(self, shoppingCart):
        self.items = shoppingCart.getItems()
        self.db.addHistory(self.userid, self.historyID, self.items)

    def getItems(self):
        return self.items