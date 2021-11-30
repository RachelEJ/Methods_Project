import ShoppingCart, PurchaseHistory

class User:
    def __init__(self, username, password, firstName, lastName, address, cardNumber):
        self.username = username
        self.password = password
        self.firstName = firstName
        self.lastName = lastName
        self.address = address
        self.cardNumber = cardNumber
        self.purchaseHistory = []
        #need to make someway to generate new ids
        self.cart = ShoppingCart.ShoppingCart(0)

    # need to add functionality
    # how do we want to access the global inventory?
    def checkout(self, cardNumber):
        self.purchaseHistory.append(PurchaseHistory(0, self.cart))
        self.cart = ShoppingCart.ShoppingCart(00)

    def getHistory(self):
        return self.purchaseHistory
    
    def changeAddresss(self, newAddress):
        self.address = newAddress

    def changePayment(self, cardNumber):
        self.cardNumber = cardNumber

    

    

            
