from models.configs import UserConfigs
import cx_Oracle

class Conection():
    def __init__(self) :
        self.user = UserConfigs()


    def testConection(self):
        try:
            self.__conection = cx_Oracle.connect(user= self.user.getUser() ,
                                password= self.user.getPassword(),
                                dsn= self.user.getDns(),
                                encoding="UTF-8")
            print("Conected")
            
        except cx_Oracle.DatabaseError as e:
            error, = e.args
            print("Oracle Database Error:", error.message)
        
    def getConection(self):
        try:
            self.__conection = cx_Oracle.connect(user= self.user.getUser() ,
                                password= self.user.getPassword(),
                                dsn= self.user.getDns(),
                                encoding="UTF-8")
            return self.__conection
            
        except cx_Oracle.DatabaseError as e:
            error, = e.args
            return("Oracle Database Error:", error.message)
        