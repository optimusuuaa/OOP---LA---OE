class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color
example = Car("toyota", "pearl white")
print("Orignal value:", example.brand, example.color)
example.color = "red"
print("Updated value:", example.brand, example.color)
example2 = Car("nissan", "blue bay")
print("Orignal value:", example2.brand, example2.color)

print("Updated value:", example2.brand, example2.color)