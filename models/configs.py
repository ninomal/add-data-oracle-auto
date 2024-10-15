
class UserConfigs():
    def __init__(self):
        self.__user = ''
        self.__password = ''
        self.__dns = ''

    def getUser(self):
        return self.__user
    
    def getPassword(self):
        return self.__password
    
    def getDns(self):
        return self.__dns