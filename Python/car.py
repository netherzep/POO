import account


class Car:
    driver    = account
    id        = int
    license   = str
    driver    = str
    __passenger = int
    
    def __init__(self, license, driver):
        self.license = license
        self.driver = driver
        
    
    def printUser(self):
        print(vars(self.driver))
        


    def getPassenger(self):
        return self.__passenger
    
    def setPassenger(self, passenger):

        if passenger < 4:
            print("Passengers amount should be greater than 3")
        else:
            self.__passenger = passenger