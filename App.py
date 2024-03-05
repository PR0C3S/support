from FtpConnection import FtpConnection
from DatabaseConnection import DatabaseConnection
from decouple import config
import pandas as pd

def convert_to_list_of_lists(lst):
    res = []
    for el in lst:
        res.append([el])
    return res

def makeFormat(lst, type):
    res = []
    for el in lst:
        if(isinstance(item, type) and type==str):
            item = el.strip().lower()
            res.append(item)
    return res

ftpServer = FtpConnection()
ftpServer.connecToFTP()
fileServer= ftpServer.downloadFile(config("FILENAME"))
ftpServer.closeFTP()

#QUERIES
createMakesTable='CREATE TABLE IF NOT EXISTS make (ID varchar(50) NOT NULL,PRIMARY KEY (ID))'
createSalesPersonTable='CREATE TABLE sIF NOT EXISTS alesperson(ID VARCHAR(50), PRIMARY KEY(ID))'
createStoresTable='CREATE TABLE IF NOT EXISTS stores(id VARCHAR(25), primary KEY(id)'
createSalesTable = '''CREATE TABLE IF NOT EXISTS sales(
    ID INTEGER,
    PriceSold FLOAT, 
    Cost FLOAT, 
    Yearsold INTEGER, 
    Mileage INTEGER, 
    Model VARCHAR(25), 
    Year INTEGER, 
    Trim VARCHAR(25), 
    Engine VARCHAR(25),
    BodyTypeVARCHAR(25),
    NumCylinders INTEGER,
    DriveType VARCHAR(25), 
    make VARCHAR(25),
    store VARCHAR(25),
    salesperson VARCHAR(50)
    primary KEY(id),
    FOREIGN KEY (make) REFERENCES make(ID),
    FOREIGN KEY (store) REFERENCES store(ID),
    FOREIGN KEY (salesperson) salesperson Persons(ID)
)'''

mysqlServer = DatabaseConnection()
mysqlServer.createDatabase(config("DB_NAME"))
mysqlServer.runQuery(createMakesTable)
mysqlServer.runQuery(createSalesPersonTable)
mysqlServer.runQuery(createStoresTable)
mysqlServer.runQuery(createSalesTable)

#Read the data
data = pd.read_csv(config("FILENAME"), skiprows=1)

#Insert all makes in make table
makes=data["Make"].values.tolist()
makes = makeFormat(makes,str)
mysqlServer.insertMany('INSERT INTO make (ID) VALUES (%s)',makes)

#Insert all stors in saleperson table
stores=data["Store"].values.tolist()
stores = makeFormat(stores,str)
mysqlServer.insertMany('INSERT INTO store (ID) VALUES (%s)',stores)

#Insert all salesperson in saleperson table
salesPersons=data["Sales_Person"].values.tolist()
salesPersons = makeFormat(salesPersons,str)
mysqlServer.insertMany('INSERT INTO salesperson (ID) VALUES (%s)',salesPersons)