import psycopg2  
import psycopg2.extras  # needed for dictionary cursor
import sys
import Item
import PurchaseHistory

import User
class DatabaseInterface():
    def __init__ (self, username, password, host, port, database):

        self.items = []
        self.users = []

        try:
            self.conn = psycopg2.connect(user = username, password = password, host = host, port = port, database=database)

            self.cursor = self.conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        except psycopg2.Error as err:
            if self.conn:
                self.conn.rollback()
            print("Could not get access to the database.")
            print("PostgreSQL Error: %s" % err.args[0])
            sys.exit(-1)

        self.loadItems()
        self.loadUsers()

    def exit(self):
        if self.conn:
            self.conn.close()
    
    
    def getItemBySku(self, sku):
        for item in self.items:
            
            if (item.sku == sku):
                return item
        return False
        
    def getUser(self, userid, password):
        for user in self.users:
            
            if (user.username == userid and user.password == password):
                return user
        return False

    def userExists(self, userid):
        for user in self.users:
            if (user.username == userid):
                return True
        return False
                
    def loadItems(self):
        try:
            
            self.cursor.execute("SELECT * FROM inventory")
            row = self.cursor.fetchone()
            while row:
                self.items.append(Item.Item(row['itemname'], row['sku'], row['price'], row['quantity'], self))
                row = self.cursor.fetchone()
            print()
            
        except psycopg2.Error as err:
            if self.conn:
                self.conn.rollback()
            print("Could not load inventory")
            print("PostgreSQL Error: %s" % err.args[0])
            sys.exit(-1)

    def loadUsers(self):
        try:
            
            self.cursor.execute("SELECT * FROM users")
            row = self.cursor.fetchone()
            while row:
                self.users.append(User.User(row['userid'], row['password'], row['fname'], row['lname'], row['email'], row['address'], row['cardinfo'], row['purchasenum'], self))
                row = self.cursor.fetchone()
            
            
        except psycopg2.Error as err:
            if self.conn:
                self.conn.rollback()
            print("Could not load users")
            print("PostgreSQL Error: %s" % err.args[0])
            sys.exit(-1)

        for user in self.users:
            try:
                grabString = "SELECT * FROM cart WHERE userid = '" + user.username +"'"
                
                
                self.cursor.execute(grabString)
                row = self.cursor.fetchone()
                while row:
                    user.cart.items.append((row['itemsku'], row['quantity']))
                    row = self.cursor.fetchone()
                
                
            except psycopg2.Error as err:
                if self.conn:
                    self.conn.rollback()
                print("Could not load cart")
                print("PostgreSQL Error: %s" % err.args[0])
                sys.exit(-1)
            
            try:
                grabString = "SELECT * FROM purchasehistory WHERE userid = '" + user.username+ "'"
                self.cursor.execute(grabString)
                row = self.cursor.fetchone()
                while row:
                    if (row['purchaseid'] in user.purchaseHistory):
                        user.purchaseHistory['purchaseid'] = PurchaseHistory.PurchaseHistory(user.username, row['purchaseid'], self)
                    user.purchaseHistory['purchaseid'].items.append((row['itemsku'], row['quantity']))
                    row = self.cursor.fetchone()
                
                
            except psycopg2.Error as err:
                if self.conn:
                    self.conn.rollback()
                print("Could not load history")
                print("PostgreSQL Error: %s" % err.args[0])
                sys.exit(-1)
                
    
    def changeItemQuantity(self, sku, quantity):
        try:
            insertString = "UPDATE inventory SET quantity = %s WHERE sku = %s"
            self.cursor.execute(insertString, (quantity, sku))
            self.conn.commit()
            
        except psycopg2.Error as err:
            if self.conn:
                self.conn.rollback()
            print("Could not change item quantity")
            print("PostgreSQL Error: %s" % err.args[0])
            sys.exit(-1)
    
    def changeUserCardInfo(self, userid, cardnum):
        try:
            insertString = "UPDATE users SET cardinfo = %s WHERE userid = %s"
            self.cursor.execute(insertString, (cardnum, userid))
            self.conn.commit()
            
        except psycopg2.Error as err:
            if self.conn:
                self.conn.rollback()
            print("Could not change user address")
            print("PostgreSQL Error: %s" % err.args[0])
            sys.exit(-1)

    def changeUserAddressInfo(self, userid, address):
        try:
            insertString = "UPDATE users SET address = %s WHERE userid = %s"
            self.cursor.execute(insertString, (address, userid))
            self.conn.commit()
            
        except psycopg2.Error as err:
            if self.conn:
                self.conn.rollback()
            print("Could not change user cardinfo")
            print("PostgreSQL Error: %s" % err.args[0])
            sys.exit(-1)

    def addUser(self, userid, fname, lname, password, email, address, cardinfo):
        if(self.userExists(userid)):
            return False
        try:
            insertString = "INSERT INTO users(userid, fname, lname, password, email, address, cardinfo, purchasenum) VALUES (%s, %s, %s, %s, %s, %s, %s, 1)"
            self.cursor.execute(insertString, (userid, fname, lname, password, email, address, cardinfo))
            self.conn.commit()
            
        except psycopg2.Error as err:
            if self.conn:
                self.conn.rollback()
            print("Could not add user\n")
            print("PostgreSQL Error: %s" % err.args[0])
            sys.exit(-1)
        self.users.append(User.User(userid, password, fname, lname, email, address, cardinfo, self))
        return True

    def removeUser(self, userid):
        try:
            # counts number of times userid appears in purchasehistory
            phString = "SELECT COUNT(*) FROM purchasehistory WHERE userid = '{0}'".format(userid)
            self.cursor.execute(phString)
            self.conn.commit()
            row = self.cursor.fetchone()
            phCount = row[0]

            # deletes all rows containing userid
            if (phCount > 0):
                phString = "DELETE FROM purchasehistory WHERE userid = '{0}'".format(userid)
                self.cursor.execute(phString)
                self.conn.commit()

            # counts number of times userid appears in cart
            cartString = "SELECT COUNT(*) FROM cart WHERE userid = '{0}'".format(userid)
            self.cursor.execute(cartString)
            self.conn.commit()
            row = self.cursor.fetchone()
            cartCount = row[0]

            # deletes all rows containing userid
            if (cartCount > 0):
                cartString = "DELETE FROM cart WHERE userid = '{0}'".format(userid)
                self.cursor.execute(cartString)
                self.conn.commit()

            # counts number of times userid appears in users
            usersString = "SELECT COUNT(*) FROM users WHERE userid = '{0}'".format(userid)
            self.cursor.execute(usersString)
            self.conn.commit()
            row = self.cursor.fetchone()
            usersCount = row[0]

            # deletes all rows containing userid
            if (usersCount > 0):
                usersString = "DELETE FROM users WHERE userid = '{0}'".format(userid)
                self.cursor.execute(usersString)
                self.conn.commit()

            return True
        
        except psycopg2.Error as err:
            if self.conn:
                self.conn.rollback()
            print("PostgreSQL Error: %s" % err.args[0])
            sys.exit(-1)

        

    def addCartItem(self, userid, sku, quantity):
        try:
            insertString = "INSERT INTO cart(userid, itemsku, quantity) VALUES (%s, %s, %s)"
            self.cursor.execute(insertString, (userid, sku, quantity))
            self.conn.commit()
            
        except psycopg2.Error as err:
            if self.conn:
                self.conn.rollback()
            print("Could not add cart item")
            print("PostgreSQL Error: %s" % err.args[0])
            sys.exit(-1)

    def removeCartItem(self, userid, sku):
        try:
            insertString = "DELETE FROM cart WHERE userid = %s AND itemsku = %s"
            self.cursor.execute(insertString, (userid, sku))
            self.conn.commit()
            
        except psycopg2.Error as err:
            if self.conn:
                self.conn.rollback()
            print("Could not remove cart item")
            print("PostgreSQL Error: %s" % err.args[0])
            sys.exit(-1)

    def emptyCart(self, userid):
        try:
            insertString = "DELETE FROM cart WHERE userid = '{0}'".format(userid)
            self.cursor.execute(insertString, (userid))
            self.conn.commit()
            
        except psycopg2.Error as err:
            if self.conn:
                self.conn.rollback()
            print("Could not empty")
            print("PostgreSQL Error: %s" % err.args[0])
            sys.exit(-1)

    def addHistory(self, userid, historyid, items):
        try:
            insertString = "INSERT INTO purchasehistory(purchaseid, userid, itemsku, quantity) VALUES (%s, %s, %s, %s)"
            self.cursor.executemany(insertString, [[historyid, userid, item[0], item[1]] for item in items ])
            self.conn.commit()
            
        except psycopg2.Error as err:
            if self.conn:
                self.conn.rollback()
            print("Could not add purchasehistory")
            print("PostgreSQL Error: %s" % err.args[0])
            sys.exit(-1)
    
