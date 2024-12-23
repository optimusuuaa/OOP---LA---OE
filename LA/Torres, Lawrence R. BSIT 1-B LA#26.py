from abc import ABC, abstractmethod

class NinjaTurle(ABC):
    @property
    @abstractmethod
    def alias(self):
        pass

class Leonardo(NinjaTurle):
    def __init__(self, real_name):
        self.real_name = real_name
        self.__alias = "leo"
   
    @property
    def alias(self):
        return self.__alias

leo = Leonardo("Leonardo")
print(leo.alias)

class Michelangelo(NinjaTurle):
    def __init__(self, real_name):
        self.real_name = real_name
        self.__alias = "angelo"
   
    @property
    def alias(self):
        return self.__alias

angelo = Michelangelo("MichelAngelo")
print(angelo.alias)

class Donatello(NinjaTurle):
    def __init__(self, real_name):
        self.real_name = real_name
        self.__alias = "brainy"
   
    @property
    def alias(self):
        return self.__alias

brainy = Donatello("Donatello")
print(brainy.alias)

class Raphael(NinjaTurle):
    def __init__(self, real_name):
        self.real_name = real_name
        self.__alias = "Raph"
   
    @property
    def alias(self):
        return self.__alias

raph = Raphael("Raphael")
print(raph.alias)