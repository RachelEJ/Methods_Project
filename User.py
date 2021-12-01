import ShoppingCart, PurchaseHistory

class User:
    def __init__(self, username, password, firstName, lastName, address, cardNumber, db):
        self.username = username
        self.password = password
        self.firstName = firstName
        self.lastName = lastName
        self.address = address
        self.cardNumber = cardNumber
        self.purchaseHistory = {}
        self.db = db
        #need to make someway to generate new ids
        self.cart = ShoppingCart.ShoppingCart(0)

    # need to add functionality
    # how do we want to access the global inventory?
    def checkout(self, cardNumber):
        self.db.emptyCart(self.username)
        self.purchaseHistory.append(PurchaseHistory(self.username, 0, self.db, self.cart))
        self.cart = ShoppingCart.ShoppingCart(00)

    def getHistory(self):
        return self.purchaseHistory
    
    def changeAddresss(self, newAddress):
        self.address = newAddress
        self.db.changeUserAddressInfo(self.username, newAddress)

    def changePayment(self, cardNumber):
        self.cardNumber = cardNumber
        self.db.changeUserCardInfo(self.username, cardNumber)

    

    

            
