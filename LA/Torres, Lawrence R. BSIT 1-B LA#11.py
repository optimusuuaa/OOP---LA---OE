class Phone:
    def __init__(self, brand,model):
        self.brand = brand
        self.model = model
       
    def describePhone(self):
        print(f"{self.brand} {self.model}.")

class Android(Phone):
    def __init__(self, brand, model):
        Phone.__init__(self, brand, model)

phone1 = Android("Samsung","Galaxy S24")
phone1.describePhone()