import mysql.connector as MS
import os

class DatabaseConnection:
    def __init__(self, host,user,pwd):
        self.conn = MS.connect(host=os.getenv("IP_DB"),user=os.getenv("ID_DB"),passwd=os.getenv("PWD_DB"))
        self.cursor = self.conn.cursor()
        pass

    def createDatabase(self,name):
        self.cursor.execute(f'create database IF NOT EXISTS {name}')
        self.conn.commit()
        print('Database create successfully')
        
    def runQuery(self,query):
        self.cursor.execute(query)
        self.conn.commit()
        print('Query execute succesfully')



conn.commit()

cursor.execute('''
		INSERT INTO products (product_id, product_name, price)
		VALUES
			(1,'Desktop Computer',800),
			(2,'Laptop',1200),
			(3,'Tablet',200),
			(4,'Monitor',350),
			(5,'Printer',150)
                ''')
