class classSection:
    def __init__(self, name, role, basic_atk):
        self.name = name
        self.role = role
        self.basic_atk = basic_atk

mm1 = classSection("Miya", "Marksman", 100)
mage = classSection("Eudora", "Mage", 80)

print("Hero Name:", mm1.name)
print("Role Attribute:", mm1.role)
print("Basic Attack:", mm1.basic_atk)
print("Hero Name:", mage.name)
print("Role Attribute:", mage.role)
print("Basic Attack:", mage.basic_atk)