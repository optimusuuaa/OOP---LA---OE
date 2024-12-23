class Car:
    def __init__(self, brand):
        self.brand = brand
    def __str__(self):
        return f"{self.brand} description"
example = Car("toyota")
print(example)
del example
print(example)
