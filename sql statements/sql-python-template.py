# Example of creating a table and inserting values

import psycopg2  
import psycopg2.extras  # needed for dictionary cursor
import sys

conn = None
try:
    conn = psycopg2.connect(user="postgres",  # same as pgAdmin
                            password="password",  # same as pgAdmin; enter your own password
                            host="127.0.0.1",
                            port="5432",
                            database="methods_store")  # same as the name of the 
                                                       # methods_store database in pgAdmin
    
    # use a dictionary to access results by column name instead of column number
    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    


    # insert multiple rows at a time
    # can be reduced to a single list for adding one row 
    insert_item = (("4001", "testInsert1", "25", "50.00"),
                     ("4002", "testInsert2", "30", "60.00"),
                     ("4003", "testInsert3", "35", "70.00"))
                    
    # postgres uses %s instead of ? as a placeholder
    insert_string = "INSERT INTO inventory(sku, itemname, quantity, price) VALUES (%s, %s, %s, %s)"
    cursor.executemany(insert_string, insert_item)
    conn.commit()  # save changes to the table

    # Basic way to run SQL statements
    cursor.execute("SELECT * FROM inventory")

    # can also create strings and then run the string
    # create_string = """SELECT * FROM inventory;"""
    # cursor.execute(create_string)
    # NOTE: postgres uses the keyword 'SERIAL' instead of 'AUTOINCREMENT'

    row = cursor.fetchone()
    while row:
        # you can either do row["columnname"] or row[0] and index it
        print(row["sku"], row["itemname"], row["quantity"], row["price"])
        row = cursor.fetchone()

except psycopg2.Error as err:
    if conn:
        conn.rollback()  # reverse any changes before the commit

    print("PostgreSQL Error: %s" % err.args[0])
    sys.exit(-1)
finally:
    if conn:
        conn.close()
