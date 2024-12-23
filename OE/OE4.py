class Character:
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power

    def attack(self, target):
        target.defend(self.power)
        print(f"{self.name} attacks {target.name}!")
        print(f"{target.name}'s remaining health: {target.health}\n")

    def defend(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0

    def special_move(self):
        raise NotImplementedError("Subclasses must implement this method.")

# Warrior Class
class Warrior(Character):
    def __init__(self, name, health, power):
        super().__init__(name, health, power)
        self.power_boosted = False

    def special_move(self):
        self.power_boosted = True
        print(f"{self.name} uses Shield Bash! Power is doubled for the next attack.\n")

    def attack(self, target):
        if self.power_boosted:
            doubled_power = self.power * 2
            target.defend(doubled_power)
            print(f"{self.name} attacks {target.name} with doubled power!")
            self.power_boosted = False  # Reset after attack
        else:
            super().attack(target)

# Mage Class
class Mage(Character):
    def special_move(self):
        print(f"{self.name} casts Fireball! It deals 100 damage to the target.\n")

    def attack(self, target):
        super().attack(target)

    def fireball(self, target):
        target.defend(100)
        print(f"{self.name} casts Fireball on {target.name}!")
        print(f"{target.name}'s remaining health: {target.health}\n")

# Archer Class
class Archer(Character):
    def special_move(self):
        print(f"{self.name} shoots a Piercing Arrow, ignoring {target.name}'s defense!\n")

    def attack(self, target):
        super().attack(target)

# Monster Class
class Monster(Character):
    def special_move(self):
        print(f"{self.name} roars and gains 58 extra health!\n")
        self.health += 58
        print(f"{self.name}'s health is now {self.health}\n")

# Simulating the Battle
def battle_simulation():
    warrior = Warrior("Warrior", 300, 50)
    mage = Mage("Mage", 200, 30)
    archer = Archer("Archer", 250, 40)
    monster = Monster("Monster", 400, 60)

    characters = [warrior, mage, archer]

    # Each character attacks and uses special move on the Monster
    for character in characters:
        character.attack(monster)
        character.special_move()

    # Monster retaliates
    for character in characters:
        monster.attack(character)
        monster.special_move()

    # Show polymorphism by calling special_move() on all characters
    print("Demonstrating polymorphism with special moves:\n")
    for character in characters + [monster]:
        character.special_move()

# Run the battle simulation
battle_simulation()