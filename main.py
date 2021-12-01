import DatabaseInterface

def createAccount(database):
    inputUsername = ""
    inputPassword = ""
    inputFName = ""
    inputLName = ""
    inputAddress = ""
    inputEmail = ""
    inputCreditCard = ""

    userLenCheck = 0
    while (userLenCheck == 0):
        inputUsername = input("Enter a username: ")
        if len(inputUsername) > 15:
            print("Please limit username to 15 characters max")
        else:
            userLenCheck = 1
    
    passLenCheck = 0
    while (passLenCheck == 0):
        inputPassword = input("Enter a password: ")
        if len(inputPassword) > 15:
            print("Please limit password to 15 characters max")
        else:
            passLenCheck = 1
    
    fnameLenCheck = 0
    while (fnameLenCheck == 0):
        inputFName = input("Enter your first name: ")
        if len(inputFName) > 15:
            print("Please limit first name to 15 characters max")
        else: 
            fnameLenCheck = 1
    
    lnameLenCheck = 0
    while (lnameLenCheck == 0):
        inputLName = input("Enter your last name: ")
        if len(inputLName) > 15:
            print("Please limit last name to 15 characters max")
        else:
            lnameLenCheck = 1
    
    addrLenCheck = 0
    while (addrLenCheck == 0):
        inputAddress = input("Enter your address: ")
        if len(inputAddress) > 30:
            print("Please limit address to 30 characters max")
        else:
            addrLenCheck = 1

    emailLenCheck = 0
    while (emailLenCheck == 0):
        inputEmail = input("Enter your email address: ")
        if len(inputEmail) > 20:
            print("Please limit email address to 20 characters max")
        else:
            emailLenCheck = 1

    cardNumLenCheck = 0
    while (cardNumLenCheck == 0):
        inputCreditCard = input("Enter your credit card number ")
        if len(inputCreditCard) > 12:
            print("Please limit credit card number to 12 characters max")
        else:
            cardNumLenCheck = 1
    database.addUser(inputUsername, inputFName, inputLName, inputPassword, inputEmail, inputAddress, inputCreditCard)
    # INSERT INTO users VALUES (inputUsername, inputfname, inputlname, inputpassword, inputemail, inputaddress, inputcreditcard)
# NOTE: database tuple has column names in this order:
# userid, fname, lname, password, email, address, cardinfo



def loginAccount(database):
    # login stuff here

    username = ""
    password = ""
    while(len(username) == 0):
        username = input("Enter username:")

    while(len(password) == 0):
        password = input("Enter password:")
    
    user = database.getUser(username, password)
    if (user == False):
        main()
    else:
        print("Logged In Successfully")
        loggedInSession(user)


def logoutAccount(user):
    # logout stuff here
    print("logout stuff here")
    main()


def viewInventory(user):
    # select * from inventory and print it out
    print("view inventory")


def addItemMenu(user):
    addItem = input("Enter the SKU of the item you wish to add ")
    quantityItem = input("Enter the quantity of that item ")
    # call the ShoppingCart method for addItem
    # if (methodCall() == 1):
    #     print("Item successfully added to cart")
    # else:
    #     print("Item was not added to cart")
    print("it has been added")


def inventoryMenu(user):
    menuOptionInvMenu = 9
    while (menuOptionInvMenu != 0):
        print("===========================")
        print("0. Go back")
        print("1. View Inventory")
        print("2. Add Item to Cart")
        menuOptionInvMenu = input("What would you like to do? ")
        print()

        if (menuOptionInvMenu == "0"):
            print("Thank you for shopping at Kastle Krashers!")
            break

        elif (menuOptionInvMenu == "1"):
            viewInventory(user)

        elif (menuOptionInvMenu == "2"):
            addItemMenu(user)

def viewCart(user):
    # select * from cart WHERE userID = (current user)
    print("view cart")

def removeItemMenu(user):
    removeItem = input("Enter the SKU of the item you wish to remove ")
    # call the ShoppingCart method for removeItem
    # if (methodCall() == 1):
    #     print("Item successfully removed from cart")
    # else:
    #     print("Item was not removed from cart")
    print("it has been removed")

def cartMenu(user):
    menuOptionCartMenu = 9
    while (menuOptionCartMenu != 0):
        print("===========================")
        print("0. Go back")
        print("1. View Cart")
        print("2. Remove Item from Cart")
        print("3. Checkout Cart")
        menuOptionCartMenu = input("What would you like to do? ")
        print()

        if (menuOptionCartMenu == "0"):
            print("Thank you for shopping at Kastle Krashers!")
            break

        elif (menuOptionCartMenu == "1"):
            viewCart(user)

        elif (menuOptionCartMenu == "2"):
            removeItemMenu(user)

        elif (menuOptionCartMenu == "3"):
            # call cart checkout method
            print("call cart checkout method")

        else:
            print("That is not a valid response. Please try again")


def viewPurchaseHistory(user):
    # select * from purchasehistory where userid == (current userID)
    print("view purchase history")


def editShippingMenu(user):
    newAddrLenCheck = 0
    while (newAddrLenCheck == 0):
        newAddress = input("Enter your new address ")
        if len(newAddress) > 30:
            print("Please limit address to 30 characters max")
        else:
            newAddrLenCheck = 1
    # UPDATE users SET address = (newAddress) WHERE userid = (current userID)



def editPaymentMenu(user):
    newCardNumLenCheck = 0
    while (newCardNumLenCheck == 0):
        newCardNum = input("Enter your new credit card number ")
        if (len(newCardNum) > 12):
            print("Please limit credit card number to 12 characters max")
        else:
            newCardNumLenCheck = 1
    # UPDATE users SET cardinfo = (newCardNum) WHERE userid = (current userID)


def deleteAccountMenu(user):
    really = "x"
    while ((really != "y") and (really != "n")):
        really = input("Are you sure you wish to delete your account? (y/n) ")
        if (really == "y"):
            verifyUser = input("Enter your username ")
            verifyPassword = input("Enter your password ")
            # call deleteAccount() class method
            break

        elif (really == "n"):
            print("Phew, you had us worried for a second there")
            break

        else:
            print("That is not a valid response. Please try again")


def accountInfoMenu(user):
    menuOptionAccInfo = 9
    while (menuOptionAccInfo != 0):
        print("===========================")
        print("0. Go back")
        print("1. Edit Shipping Address")
        print("2. Edit Payment Information")
        print("3. Delete Account")
        menuOptionAccInfo = input("What would you like to do? ")
        print()

        if (menuOptionAccInfo == "0"):
            print("Thank you for shopping at Kastle Krashers!")
            break

        elif (menuOptionAccInfo == "1"):
            editShippingMenu()

        elif (menuOptionAccInfo == "2"):
            editPaymentMenu()
        
        elif (menuOptionAccInfo == "3"):
            deleteAccountMenu()

        else:
            print("That is not a valid response. Please try again")


def userMenu(user):
    menuOptionUserMenu = 9
    while (menuOptionUserMenu != 0):
        print("===========================")
        print("0. Go back")
        print("1. View Purchase History")
        print("2. View Account Information")
        menuOptionUserMenu = input("What would you like to do? ")
        print()

        if (menuOptionUserMenu == "0"):
            print("Thank you for shopping at Kastle Krashers!")
            break

        elif (menuOptionUserMenu == "1"):
            viewPurchaseHistory(user)

        elif (menuOptionUserMenu == "2"):
            accountInfoMenu(user)

        else:
            print("That is not a valid response. Please try again")


def loggedInSession(user):
    menuOptionLoggedIn = 9
    while (menuOptionLoggedIn != 0):
        print("===========================")
        print("0. Exit Program")
        print("1. Inventory Information")
        print("2. Cart Information")
        print("3. User Information")
        print("4. Logout")
        menuOptionLoggedIn = input("What would you like to do? ")
        print()

        if (menuOptionLoggedIn == "0"):
            print("Thank you for shopping at Kastle Krashers!")
            quit()

        elif (menuOptionLoggedIn == "1"):
            inventoryMenu(user)

        elif (menuOptionLoggedIn == "2"):
            cartMenu(user)

        elif (menuOptionLoggedIn == "3"):
            userMenu(user)

        elif (menuOptionLoggedIn == "4"):
            logoutAccount(user)

        else:
            print("That is not a valid response. Please try again")


def main():
    print("Welcome to Kastle Krashers!")
    print()
    menuOptionMain = 911
    database = DatabaseInterface.DatabaseInterface("postgres", "flameMonkey", "127.0.0.1", "5432", "methods_store")
    while (menuOptionMain != 0):
        print("===========================")
        print("0. Exit Program")
        print("1. Create Account")
        print("2. Login")
        menuOptionMain = input("What would you like to do? ")
        print()

        if (menuOptionMain == "0"):
            print("Thank you for shopping at Kastle Krashers!")
            quit()
        
        elif (menuOptionMain == "1"):
            createAccount(database)
        
        elif (menuOptionMain == "2"):
            loginAccount(database)

        else:
            print("That is not a valid response. Please try again")

main()
