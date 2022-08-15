from Python.payment import Payment

class PayPal(Payment):
    
    def __init__(self, id):
        super().__init__(id)