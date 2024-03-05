from ftplib import FTP
from decouple import config

class FtpConnection:
    def __init__(self):
        self.ftp = FTP()
        pass
    
    def connecToFTP(self):
        self.ftp.connect(config("FTP_SITE"), 21)
        self.ftp.login(config("FTP_ID"), config("FTP_PWD"))
        print(self.ftp.getwelcome())
        print('Connected to FTP server')
        
    def getListDir(self):
        return self.ftp.dir()

    def closeFTP(self):
        self.ftp.close()
        print('Disconnected from FTP server')
        
    def downloadFile(self,fileObjectName):
        with open(fileObjectName, "wb") as file:
            # Command for Downloading the file "RETR filename"
            self.ftp.retrbinary(f"RETR {fileObjectName}", file.write)
        file= open(fileObjectName, "r")
        print('File download from the server')
        return file