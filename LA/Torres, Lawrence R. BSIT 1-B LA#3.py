class classSection:
    def __init__(self, name, role, basic_atk):
        self.name = name
        self.role = role
        self.basic_atk = basic_atk

    def whoMe(self):
        return f"{self.name} is a {self.role} hero and has a basic attack of {self.basic_atk}."

mm1 = classSection("Layla", "Marksman", 100)

print("Hero Name:", mm1.name)
print("Role Attribute:", mm1.role)
print("Basic Attack:", mm1.basic_atk)
print(mm1.whoMe())
