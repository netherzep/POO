from Python.car import Car


class UberVan(Car):
    typeCarAccepted = []
    SeatsMaterial = []

    def __init__(self, license, driver, typeCarAccepted, SeatsMaterial):
        super().__init__(license, driver)
        self.typeCarAccepted = typeCarAccepted
        self.SeatsMaterial = SeatsMaterial