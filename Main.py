from FtpConnection import FtpConnection
#from DatabaseConnection import DatabaseConnection
from dotenv import load_dotenv
import os

load_dotenv()

ftpServer = FtpConnection()
ftpServer.connecToFTP()
print(ftpServer.getListDir())
fileServer= ftpServer.downloadFile(os.getenv("FILENAMEFTP"))
ftpServer.closeFTP()

#mysqlServer = DatabaseConnection()
#mysqlServer.createDatabase(os.getenv("DB"))

