import DatabaseInterface
from ShoppingCart import ShoppingCart

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
    if (database.addUser(inputUsername, inputFName, inputLName, inputPassword, inputEmail, inputAddress, inputCreditCard)):
        print("Successfully created user.\n")
    else:
        print("Could not add user - username already taken.")
    # INSERT INTO users VALUES (inputUsername, inputfname, inputlname, inputpassword, inputemail, inputaddress, inputcreditcard)
# NOTE: database tuple has column names in this order:
# userid, fname, lname, password, email, address, cardinfo


def loginAccount(database):
    username = ""
    password = ""
    while(len(username) == 0):
        username = input("Enter username: ")

    while(len(password) == 0):
        password = input("Enter password: ")
    
    user = database.getUser(username, password)
    if (user == False):
        print("Did not find a match.\n")
        main(database)
    else:
        print("Logged In Successfully\n")
        loggedInSession(user, database)


def logoutAccount(user, database):
    print("You have been logged out\n")
    main(database)


def viewInventory(user, database):
    for item in database.items:
        inStockText = 'In Stock: ' + str(item.quantity)
        if (item.quantity < 0):
            inStockText = "Out of Stock"
        print( item.name, 'SKU:', item.sku, 'Price:', "???"+str(item.price), inStockText)


def addItemMenu(user, database):
    addItem = input("Enter the SKU of the item you wish to add: ")
    quantityItem = int(input("Enter the quantity of that item: "))

    if(user.cart.addItem(addItem, quantityItem)):
        print ("Successfully added item.\n")
    
    else:
        print("Could not add item.\n")


def inventoryMenu(user, database):
    print("===========================")
    print("Inventory Information")
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
            viewInventory(user, database)

        elif (menuOptionInvMenu == "2"):
            addItemMenu(user, database)


def viewCart(user, database):
    if (len(user.cart.items) == 0):
        print("Cart is empty.")
    for item in user.cart.items:
        actualItem = database.getItemBySku(item[0])
        print(actualItem.name, "SKU:" , item[0], "Quantity:", item[1], "Cost:", actualItem.price * int(item[1]))
    print()


def removeItemMenu(user, database):
    removeItem = input("Enter the SKU of the item you wish to remove: ")
    if(user.cart.removeItem(removeItem)):
        print ("Successfully removed item.\n")
    
    else:
        print("Could not remove item.\n")


def checkoutCart(user, database):
    if (len(user.cart.items) == 0):
        print("Cart is empty.")
    else:
        if(True): # call the checkout stuff here somehow
            user.checkout()
            print ("Successfully checked out items.\n")
        else:
            print("Could not check out items.\n")


def cartMenu(user, database):
    print("===========================")
    print("Cart Information")
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
            viewCart(user, database)

        elif (menuOptionCartMenu == "2"):
            removeItemMenu(user, database)

        elif (menuOptionCartMenu == "3"):
            checkoutCart(user, database)

        else:
            print("That is not a valid response. Please try again\n")


def viewPurchaseHistory(user, database):
    # select * from purchasehistory where userid == (current userID)
    
    for historyItem in user.purchaseHistory:
        print("Purchase:", user.purchaseHistory[historyItem].historyID)
        for item in user.purchaseHistory[historyItem].items:
            actualItem = database.getItemBySku(item[0])
            print(actualItem.name, "SKU:" , item[0], "Quantity:", item[1], "Cost:", actualItem.price * int(item[1]))


def deleteAccount(user, database):
    removeID = user.getUsername()
    if (database.removeUser(removeID)):
        print("Successfully deleted account.\n")
        main()
    else:
        print("Failed to delete account.\n")


def editShippingMenu(user, database):
    newAddrLenCheck = 0
    while (newAddrLenCheck == 0):
        newAddress = input("Enter your new address: ")
        if len(newAddress) > 30:
            print("Please limit address to 30 characters max")
        else:
            newAddrLenCheck = 1
    user.changeAddress(newAddress)


def editPaymentMenu(user, database):
    newCardNumLenCheck = 0
    while (newCardNumLenCheck == 0):
        newCardNum = input("Enter your new credit card number: ")
        if (len(newCardNum) > 12):
            print("Please limit credit card number to 12 characters max")
        else:
            newCardNumLenCheck = 1
    user.changePayment(newCardNum)


def deleteAccountMenu(user, database):
    really = "x"
    while ((really != "y") and (really != "n")):
        really = input("Are you sure you wish to delete your account? (y/n) ")
        if (really == "y"):
            deleteAccount(user, database)

        elif (really == "n"):
            print("Phew, you had us worried for a second there\n")
            break

        else:
            print("That is not a valid response. Please try again\n")


def accountInfoMenu(user, database):
    print("===========================")
    print("Account Information")
    print("Address: ", user.address)
    print("Email: ", user.email)
    print("Credit Card Number: ", user.cardNumber)

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
            editShippingMenu(user, database)

        elif (menuOptionAccInfo == "2"):
            editPaymentMenu(user, database)
        
        elif (menuOptionAccInfo == "3"):
            deleteAccountMenu(user, database)

        else:
            print("That is not a valid response. Please try again\n")


def userMenu(user, database):
    print("===========================")
    print("User Information")
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
            viewPurchaseHistory(user, database)

        elif (menuOptionUserMenu == "2"):
            accountInfoMenu(user, database)

        else:
            print("That is not a valid response. Please try again\n")


def loggedInSession(user, database):
    print("===========================")
    print("Main Menu")
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
            inventoryMenu(user, database)

        elif (menuOptionLoggedIn == "2"):
            cartMenu(user, database)

        elif (menuOptionLoggedIn == "3"):
            userMenu(user, database)

        elif (menuOptionLoggedIn == "4"):
            logoutAccount(user, database)

        else:
            print("That is not a valid response. Please try again\n")


def main(database = None):
    print("===========================")
    print("Welcome to Kastle Krashers!")
    menuOptionMain = 911
    if (database == None):
        #Make sure to change the password to your database password for main to work.
        database = DatabaseInterface.DatabaseInterface("postgres", "password", "127.0.0.1", "5432", "methods_store")
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
            print("That is not a valid response. Please try again\n")

main()
