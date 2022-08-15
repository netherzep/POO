from car import Car
from account import Account

if __name__ == "__main__":
    
    print("Hola Mundo")
    car = Car("ASD458",Account("Diego Llanos","1022403530"))
    car.passenger = 4
    print(vars(car.driver))

    car2 = Car("AIY458",Account("Karen García","1071304231"))
    car2.passenger = 4
    print(vars(car2.driver))
