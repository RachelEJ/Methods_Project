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

    def exit(self):
        if self.conn:
            self.conn.close()
    

    def loadItems(self):
        try:
            
            self.cursor.execute("SELECT * FROM inventory")
            row = self.cursor.fetchone()
            while row:
                self.items.append(Item.Item(row['name'], row['sku'], row['price'], row['quantity'], self))
                row = self.cursor.fetchone()
            
            
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
                self.users.append(User.User(row['userid'], row['password'], row['fname'], row['lname'], row['address'], row['cardinfo'], self))
                row = self.cursor.fetchone()
            
            
        except psycopg2.Error as err:
            if self.conn:
                self.conn.rollback()
            print("Could not load users")
            print("PostgreSQL Error: %s" % err.args[0])
            sys.exit(-1)

        for user in self.users:
            try:
                self.cursor.execute("SELECT * FROM cart WHERE userid = %s", (user.username))
                row = self.cursor.fetchone()
                while row:
                    user.cart.addItem(row['itemsku'], row['quantity'])
                    row = self.cursor.fetchone()
                
                
            except psycopg2.Error as err:
                if self.conn:
                    self.conn.rollback()
                print("Could not load cart")
                print("PostgreSQL Error: %s" % err.args[0])
                sys.exit(-1)
            
            try:
                self.cursor.execute("SELECT * FROM purchasehistory WHERE userid = %s", (user.username))
                row = self.cursor.fetchone()
                while row:
                    if (row['purchaseid'] in user.purchaseHistory):
                        user.purchaseHistory['purchaseid'] = PurchaseHistory.PurchaseHistory(user.username, row['purchaseid'], self)
                    user.purchaseHistory['purchaseid'].addItem(row['itemsku'], row['quantity'])
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

    def addCartItem(self, userid, sku, quantity):
        try:
            insertString = "INSERT INTO cart(userid, itemsku, quantity) VALUES %s %s %s"
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
            insertString = "DELETE FROM cart WHERE userid = %s AND sku = %s"
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
            insertString = "DELETE FROM cart WHERE userid = %s"
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
            insertString = "INSERT INTO purchasehistory(purchaseid, userid, itemsku, quantity) VALUES %s %s %s %s"
            self.cursor.executemany(insertString, [[historyid, userid, item[0], item[1]] for item in items ])
            self.conn.commit()
            
        except psycopg2.Error as err:
            if self.conn:
                self.conn.rollback()
            print("Could not add purchasehistory")
            print("PostgreSQL Error: %s" % err.args[0])
            sys.exit(-1)
    

    



