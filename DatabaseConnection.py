import mysql.connector as MS
from decouple import config

class DatabaseConnection:
    def __init__(self):
        self.conn = MS.connect(host=config("DB_IP"),user=config("DB_ID"),passwd=config("DB_PWD"))
        self.cursor = self.conn.cursor()
        pass

    def createDatabase(self,name):
        self.cursor.execute(f'create database IF NOT EXISTS {name}')
        self.conn.commit()
        self.conn.database = name
        print('Database create successfully')
        
    def runQuery(self,query):
        cursor = self.conn.cursor()
        cursor.execute(query)
        print('Query execute succesfully')
        
    def insertMany(self,query,values):
        self.cursor = self.conn.cursor()
        self.cursor.executemany(query,values)
        self.conn.commit()
        print(self.cursor.rowcount, "was inserted.")
    def insertOne(self,query,values):
        self.cursor = self.conn.cursor()
        self.cursor.execute(query,values)
        self.conn.commit()
        print("The data was inserted.")


