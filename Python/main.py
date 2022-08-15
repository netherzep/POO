from car import Car

if __name__ == "__main__":
    print("Hola Mundo")
    car = Car()
    car.license = "ASD458"
    car.driver = "Diego Llanos"
    car.passenger = 4
    print(vars(car))

    car2 = Car()
    car2.license = "AIY458"
    car2.driver = "Karen Garcia"
    car2.passenger = 4
    print(vars(car2))
