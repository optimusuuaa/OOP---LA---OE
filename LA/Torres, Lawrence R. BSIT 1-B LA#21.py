class Fav_food:
    def __init__(self, name, ingredient1, ingredient2, ingredient3):
        self.__name = name
        self.ingredient1 = ingredient1
        self._ingredient2 = ingredient2
        self.__ingredient3 = ingredient3

    def __str__(self):
        return f"My favorite food {self.__name} and here are the ingredients {self.__ingredient1}, {self.__ingredient2}, {self.__ingredient3}."

    def get_beated(self, age):
        if age > 15:
            return self.__ingredient3
        else:
            return "Secret!"

    def update(self, bago, nanay_ka_ba):
        if nanay_ka_ba == "oo":
            self.__ingredient3 = bago
            return "Update Success!"
        else:
            return "Bawal!"

garlic_butter_shrimp = Fav_food("garlic butter shrimp","2kg of shrimp", "2 parshley", "1/4 cup butter")
print(garlic_butter_shrimp.update("1/2 cup butter", "oo"))
print(garlic_butter_shrimp.get_beated(16))
