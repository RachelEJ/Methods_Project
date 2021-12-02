import ShoppingCart, PurchaseHistory

class User:
    def __init__(self, username, password, firstName, lastName, email, address, cardNumber, currPurchaseNum, db):
        self.username = username
        self.password = password
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.address = address
        self.cardNumber = cardNumber
        self.purchaseHistory = {}
        self.db = db
        self.currPurchaseNum = currPurchaseNum

        #need to make someway to generate new ids
        self.cart = ShoppingCart.ShoppingCart(username, db)

    def checkout(self):
        self.db.emptyCart(self.username)
        for item in self.cart.items:
            actualItem = self.db.getItemBySku(item[0])
            actualItem.changeQuantity(actualItem.quantity - item[1])
        self.purchaseHistory[self.currPurchaseNum] = (PurchaseHistory.PurchaseHistory(self.username, self.currPurchaseNum, self.db, self.cart))
        self.cart = ShoppingCart.ShoppingCart(self.username, self.db)
        self.currPurchaseNum += 1
        self.db.savePurchaseNumIncrease(self.username, self.currPurchaseNum)
        
    def getUsername(self):
        return self.username

    def getHistory(self):
        return self.purchaseHistory
    
    def changeAddress(self, newAddress):
        self.address = newAddress
        self.db.changeUserAddressInfo(self.username, newAddress)

    def changePayment(self, cardNumber):
        self.cardNumber = cardNumber
        self.db.changeUserCardInfo(self.username, cardNumber)
