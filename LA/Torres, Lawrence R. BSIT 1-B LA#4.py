class classSection:
    def __init__(self, name, role, basic_atk):
        self.name = name
        self.role = role
        self.basic_atk = basic_atk

    def whoMe(self):
        return f"{self.name} is a {self.role} hero and has a basic attack of {self.basic_atk}."

    def __str__(self):
        return f"{self.name} is a {self.role} hero."

mm1 = classSection("Layla", "Marksman", 100)

print(mm1)
