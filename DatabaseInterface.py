import psycopg2  
import psycopg2.extras  # needed for dictionary cursor
import sys
import Item
import PurchaseHistory
import ShoppingCart
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
                self.items.append(Item.Item(row['name'], row['sku'], row['price'], row['quantity']))
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
                self.users.append(User.User(row['userid'], row['password'], row['fname'], row['lname'], row['address'], row['cardinfo']))
                row = self.cursor.fetchone()
            
            
        except psycopg2.Error as err:
            if self.conn:
                self.conn.rollback()
            print("Could not load users")
            print("PostgreSQL Error: %s" % err.args[0])
            sys.exit(-1)

        for user in self.users:
            try:
                self.cursor.execute("SELECT * FROM cart WHERE userid = %", (user.username))
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
                self.cursor.execute("SELECT * FROM purchasehistory WHERE userid = %", (user.username))
                row = self.cursor.fetchone()
                while row:
                    if (row['purchaseid'] in user.purchaseHistory):
                        user.purchaseHistory['purchaseid'] = PurchaseHistory.PurchaseHistory(row['purchaseid'])
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
            insertString = "UPDATE inventory SET quantity = % WHERE sku = %"
            self.cursor.execute(insertString, (sku, quantity))
            self.conn.commit()
            
        except psycopg2.Error as err:
            if self.conn:
                self.conn.rollback()
            print("Could not change item Quantity")
            print("PostgreSQL Error: %s" % err.args[0])
            sys.exit(-1)

    



