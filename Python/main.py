from car import Car
from account import Account

if __name__ == "__main__":
    
    print("Hola Mundo")
    uberx = Car("ASD458",Account("Diego Llanos","1022403530"))
    uberx.setPassenger(4)
    uberx.printUser()
    print("Passengers: " + str(uberx.getPassenger()))

