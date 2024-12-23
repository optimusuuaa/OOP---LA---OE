class Toy:
    def __init__(self, name,price):
        self.name = name
        self.price = price
       
    def toyDetails(self):
        print(f"{self.name} costs {self.price}.")

class Car(Toy):
    def __init__(self, name, price):
        super().__init__(name, price)

toy1 = Car("XBOX","₱10,000")
toy1.toyDetails()